from django.shortcuts import render
import pickle
import numpy as np
import os
import csv
from django.conf import settings

# Load model
model_path = os.path.join(settings.BASE_DIR, 'price_model.pkl')
model = pickle.load(open(model_path, 'rb'))

# Define CSV file path
data_log_path = os.path.join(settings.BASE_DIR, 'new_data.csv')

# Ensure file exists with headers
if not os.path.exists(data_log_path):
    with open(data_log_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['feature1', 'feature2', 'feature3', 'predicted_price'])

def predict(request):
    predicted_price = None

    if request.method == 'POST':
        try:
            # Get user input
            feature1 = float(request.POST.get('feature1'))
            feature2 = float(request.POST.get('feature2'))
            feature3 = float(request.POST.get('feature3'))

            # Predict
            features = np.array([[feature1, feature2, feature3]])
            prediction = model.predict(features)
            predicted_price = round(prediction[0], 2)

            # ✅ Save inputs and prediction to CSV
            with open(data_log_path, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([feature1, feature2, feature3, predicted_price])

        except Exception as e:
            predicted_price = f"Error: {e}"

    return render(request, 'predictor/predict.html', {'predicted_price': predicted_price})
