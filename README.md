# AQI Prediction using Machine Learning

This repository contains a machine learning model for predicting Air Quality Index (AQI) based on various environmental parameters. The model leverages historical air pollution data to provide accurate AQI predictions, aiding in air quality monitoring and management.

## 🚀 Features
- Data preprocessing and cleaning
- Exploratory Data Analysis (EDA) for insights
- Machine Learning model training and evaluation
- Predictive analytics for AQI forecasting
- Web-based interface for predictions

## 📂 Repository Structure
```
📁 AQI-Prediction-ML
│-- 📂 backend           # Backend server and templates
│   │-- 📂 templates     # HTML templates for web UI
│   │   │-- index.html  # Input form for AQI prediction
│   │   │-- result.html # Displaying prediction results
│   │-- server.py       # Flask server script
│-- 📜 AQI-prediction.ipynb  # Jupyter notebook for ML model
│-- 📜 AQI_data.csv          # Dataset file
│-- 📜 model_coefficients.txt # Model parameters
│-- 📜 requirements.txt      # Dependencies
│-- 📜 README.md            # Project documentation
```

## 📊 Dataset
The dataset consists of historical air pollution data, including factors like:
- PM2.5, PM10, NO2, SO2, CO, O3 concentrations

## 🔧 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Kr1shnendu/AQI-Prediction-ML.git
   cd AQI-Prediction-ML
   ```
2. Install dependencies:
   ```bash
   pip install flask
   ```
3. Run the backend server:
   ```bash
   python backend/server.py
   ```

## 🛠️ Usage
- Access the web UI via `http://127.0.0.1:5000/` after starting the server.
- Modify `AQI-prediction.ipynb` for custom model training.
- Store AQI data in `AQI_data.csv` for predictions.

## 📈 Model
The machine learning model used includes:
- Linear Regression
- Feature engineering for better predictive performance
- Model evaluation using RMSE and R² scores

## 🔮 Future Improvements
- Integration with real-time air quality sensors
- Deployment as a web-based API
- Advanced deep learning models for better accuracy

## 📜 License
This project is licensed under the MIT License.

## 🤝 Contributing
Feel free to submit issues or pull requests if you have improvements!

## 📬 Contact
For queries, reach out via GitHub Issues.

🔗 **GitHub Repository:** [AQI-Prediction-ML](https://github.com/Kr1shnendu/AQI-Prediction-ML)

