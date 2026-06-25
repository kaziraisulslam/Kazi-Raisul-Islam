# compliance-engine/Enterprise-Layer/CCM/drift_monitor.py
import json
import time

def monitor_model_telemetry(current_bias_score, current_latency_ms):
    """
    Simulates real-time telemetry verification for Article 10 & 15.
    """
    BIAS_LIMIT = 0.05
    LATENCY_LIMIT = 250.0  # ms
    
    alert_triggered = False
    failure_reasons = []
    
    if current_bias_score > BIAS_LIMIT:
        alert_triggered = True
        failure_reasons.append(f"Bias drift detected: {current_bias_score} exceeds legal limit of {BIAS_LIMIT} (Art 10)")
        
    if current_latency_ms > LATENCY_LIMIT:
        alert_triggered = True
        failure_reasons.append(f"System degradation: Latency {current_latency_ms}ms exceeds robustness limit (Art 15)")
        
    telemetry_payload = {
        "metric_timestamp": int(time.time()),
        "status": "CRITICAL_ALERT" if alert_triggered else "OPERATIONAL",
        "telemetry": {
            "bias_metric": current_bias_score,
            "latency_ms": current_latency_ms
        },
        "violations": failure_reasons
    }
    
    return telemetry_payload

if __name__ == "__main__":
    # Simulate a drift event
    print(json.dumps(monitor_model_telemetry(0.07, 180.0), indent=2))
