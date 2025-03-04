from flask import Flask, render_template, request
import numpy as np
import math

app = Flask(__name__)

# Load model coefficients from the text file
with open('model_coefficients.txt', 'r') as f:
    lines = f.readlines()
    intercept = float(lines[0].split(": ")[1])  # Load the intercept
    coefficients = {}
    for line in lines[1:]:  # Load coefficients for each feature
        key, value = line.strip().split(": ")
        coefficients[key] = float(value)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get input values from the form
        input_data = [
            float(request.form['CO']),
            float(request.form['Ozone']),
            float(request.form['PM10']),
            float(request.form['PM25']),
            float(request.form['NO2'])
        ]

        # Calculate the prediction using the model coefficients
        prediction = intercept
        for i, key in enumerate(coefficients.keys()):
            prediction += coefficients[key] * input_data[i]

        
        # Air quality categories
        air_quality_categories = {
            'Good': (0, 50),
            'Moderate': (51, 100),
            'Poor': (101, 150),
            'Unhealthy': (151, 200),
            'Severe': (201, 300),
            'Hazardous': (301, float('inf'))
        }

        # Function to determine air quality category
        def get_air_quality_category(prediction):
            for category, (lower, upper) in air_quality_categories.items():
                if lower <= prediction <= upper:
                    return category



        return render_template('result.html', prediction=math.ceil(prediction * 100) / 100, category=get_air_quality_category(prediction))

if __name__ == '__main__':
    app.run(debug=True)