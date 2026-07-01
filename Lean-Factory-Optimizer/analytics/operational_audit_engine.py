# analytics/operational_audit_engine.py
import os
import pandas as pd

def analyze_factory_efficiency(input_csv, output_excel, energy_cost_per_kwh=0.15):
    """
    Ingests factory floor operational telemetry, calculates Lean waste metrics,
    and exports a financial margin impact workbook for management.
    """
    if not os.path.exists(input_csv):
        print(f"❌ Error: Source telemetry file {input_csv} not found.")
        return False

    print(f"🔄 Ingesting production floor telemetry...")
    df = pd.read_csv(input_csv)
    
    # Standardize data inputs
    df.columns = [col.strip().upper() for col in df.columns]
    
    # Calculate operational metrics: Scrap Rate and Specific Energy Consumption
    df['SCRAP_RATE_PCT'] = (df['SCRAP_UNITS'] / df['TOTAL_UNITS_PRODUCED']) * 100
    df['ENERGY_PER_UNIT_KWH'] = df['ENERGY_CONSUMPTION_KWH'] / df['TOTAL_UNITS_PRODUCED']
    df['WASTE_COST_EUR'] = (df['SCRAP_UNITS'] * df['UNIT_MATERIAL_COST']) + (df['ENERGY_CONSUMPTION_KWH'] * energy_cost_per_kwh)
    
    # Isolate shifts operating outside efficient target margins (e.g., Scrap Rate > 4%)
    inefficient_shifts = df[df['SCRAP_RATE_PCT'] > 4.0].copy()
    
    print(f"🚨 Audit complete: Identified {len(inefficient_shifts)} shifts exceeding waste thresholds.")
    
    # Generate clean Excel workbook for executive review
    with pd.ExcelWriter(output_excel, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Master Operations Audit', index=False)
        inefficient_shifts.to_excel(writer, sheet_name='Actionable Waste Alerts', index=False)
        
    print(f"✅ Executive financial report exported safely to: {output_excel}")
    return True

if __name__ == "__main__":
    # Internal test harness configuration pathing
    mock_source = "../data_models/factory_floor_telemetry.csv"
    mock_report = "../data_models/financial_margin_impact.xlsx"
    
    if os.path.exists(mock_source):
        analyze_factory_efficiency(mock_source, mock_report)
