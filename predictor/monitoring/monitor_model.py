import numpy as np
from predictor.models import PredictionLog
from sklearn.metrics import mean_absolute_error, mean_squared_error

def evaluate_model_performance():
    logs = PredictionLog.objects.exclude(actual_price__isnull=True)
    if not logs.exists():
        print("No data with actual values yet.")
        return

    y_true = [log.actual_price for log in logs]
    y_pred = [log.predicted_price for log in logs]

    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))

    print(f"📊 Model Monitoring Report")
    print(f"MAE: {mae:.3f}")
    print(f"RMSE: {rmse:.3f}")

    if mae > 10:  # example threshold
        print("⚠️ Model performance degraded — consider retraining!")
