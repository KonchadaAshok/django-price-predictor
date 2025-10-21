import pandas as pd
from scipy.stats import ks_2samp
from predictor.models import PredictionLog

def detect_drift(reference_data, new_data):
    drift_results = {}
    for col in reference_data.columns:
        stat, p_value = ks_2samp(reference_data[col], new_data[col])
        drift_results[col] = (p_value < 0.05)  # True means drift detected
    return drift_results

def monitor_data_drift():
    logs = PredictionLog.objects.all().order_by('timestamp')
    df = pd.DataFrame(list(logs.values('feature1', 'feature2', 'feature3')))

    if len(df) < 100:
        print("Not enough data to monitor drift.")
        return

    reference = df.iloc[:50]
    recent = df.iloc[-50:]

    drift = detect_drift(reference, recent)
    print("🚨 Drift Report:", drift)
