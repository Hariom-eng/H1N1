H1N1 & Seasonal Flu Vaccine Prediction:

Overview:
This project builds an SVM (Support Vector Machine) model to predict whether individuals received the H1N1 vaccine and the seasonal flu vaccine based on various features.

Dataset:
The dataset consists of 26,707 rows and 35 columns.
Key features include health behaviors, doctor recommendations, demographics, and opinions on vaccines, behavioral.

Target variables:
1.h1n1_vaccine (0: No, 1: Yes)
2.seasonal_vaccine (0: No, 1: Yes)

Model:
1.Support Vector Machine (SVM) with a linear kernel.
2.Feature Scaling using StandardScaler.
3.Encoding categorical variables using Label Encoding.
4.Train-Test Split (80% training, 20% testing).

Performance:
H1N1 Vaccine Prediction Accuracy: 
Seasonal Flu Vaccine Prediction Accuracy: 
Evaluation Metrics: Accuracy, Precision, Recall, F1-score

Results:
The model performs better on seasonal flu vaccine predictions.
The H1N1 vaccine prediction is more challenging due to class imbalance.
