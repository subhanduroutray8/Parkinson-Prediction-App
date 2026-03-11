# Parkinson-Prediction-App

This project presents a machine learning–based system that predicts the severity of Parkinson’s disease using biomedical voice measurements. The model analyzes multiple voice-related features and estimates disease severity using the Unified Parkinson’s Disease Rating Scale (UPDRS).

The project is built using Python and common data science libraries including Pandas, NumPy, Scikit-learn, and Streamlit. A Random Forest Regressor model was trained on the Parkinson’s Telemonitoring Dataset to learn patterns between voice measurements and disease severity. The trained model can predict Parkinson’s severity based on new patient input data.

The workflow of this project includes data preprocessing, exploratory data analysis, feature selection, model training, evaluation, and deployment of a simple web-based prediction system. Model performance was evaluated using metrics such as Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R² score to ensure accurate predictions.

To make the model accessible and interactive, a Streamlit web application was developed. The web interface allows users to input patient features such as age, sex, jitter, shimmer, and other voice-related parameters. After entering the data, the model instantly predicts the Parkinson’s severity score.

This project demonstrates how machine learning can be applied to healthcare data to assist in early monitoring and assessment of neurological diseases. It also showcases a complete end-to-end machine learning pipeline from data analysis to model deployment.

Key Technologies Used:

* Python
* Pandas and NumPy
* Scikit-learn
* Random Forest Regressor
* Streamlit
* Jupyter Notebook

The goal of this project is to explore the application of artificial intelligence in healthcare and provide a simple tool that demonstrates how voice analysis can help estimate Parkinson’s disease severity.
