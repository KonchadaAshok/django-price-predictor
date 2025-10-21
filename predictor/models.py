from django.db import models

class PredictionLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    feature1 = models.FloatField()
    feature2 = models.FloatField()
    feature3 = models.FloatField()
    predicted_price = models.FloatField()
    actual_price = models.FloatField(null=True, blank=True)  # optional, filled later

    def __str__(self):
        return f"Prediction on {self.timestamp}: {self.predicted_price}"
