# Logistics-Data-Triage/src/inventory_triage_engine.py
import os
import pandas as pd

def run_inventory_triage(input_csv, output_excel, safety_threshold=15):
    """
    Ingests raw warehouse manifests, filters for critical low-stock items,
    and exports a structured Excel dispatch report for shift supervisors.
    """
    if not os.path.exists(input_csv):
        print(f"❌ Error: Input manifest {input_csv} not found.")
        return False
        
    print(f"🔄 Ingesting raw shop-floor data manifest: {input_csv}")
    
    # Ingest data safely handling potential structural formatting variations
    df = pd.read_csv(input_csv)
    
    # Standardize column headers for production systems
    df.columns = [col.strip().upper() for col in df.columns]
    
    # Check for core required logistics metrics
    required_fields = ["PART_ID", "PART_NAME", "CURRENT_STOCK", "LOCATION_AISLE"]
    for field in required_fields:
        if field not in df.columns:
            raise KeyError(f"Missing mandatory enterprise field: {field}")
            
    # Execute deterministic rule-based filtering for low-stock anomalies
    critical_shortages = df[df["CURRENT_STOCK"] <= safety_threshold].copy()
    
    # Calculate operational deficit levels
    critical_shortages["DEFICIT_VOLUME"] = safety_threshold - critical_shortages["CURRENT_STOCK"]
    
    # Sort by urgency level
    critical_shortages = critical_shortages.sort_values(by="CURRENT_STOCK", ascending=True)
    
    print(f"🚨 Triage complete: Found {len(critical_shortages)} critical material shortages.")
    
    # Export clean multi-sheet operational workbook using openpyxl engine
    with pd.ExcelWriter(output_excel, engine='openpyxl') as writer:
        critical_shortages.to_excel(writer, sheet_name='Actionable Shortages', index=False)
        df.to_excel(writer, sheet_name='Full Master Inventory', index=False)
        
    print(f"✅ Optimized dispatch report generated: {output_excel}")
    return True

if __name__ == "__main__":
    # Test harness execution mapping to mock local files
    mock_csv = "../data/raw_inbound_manifest.csv"
    mock_output = "../data/optimized_dispatch_report.xlsx"
    
    # Execute dummy run if configuration environment setup is met
    if os.path.exists(mock_csv):
        run_inventory_triage(mock_csv, mock_output)
