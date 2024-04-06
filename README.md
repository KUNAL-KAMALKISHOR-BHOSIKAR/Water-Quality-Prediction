# Water Quality Prediction System

This project is a water quality prediction system developed for Omdena's Rwanda Chapter. The system utilizes the Streamlit framework to provide an interactive user interface for predicting water quality in different locations.<br>
You can access the web app using this link: [Water Quality Prediction System](https://water-quality-prediction-app.streamlit.app)

## Project Overview

The goal of this project is to develop a machine learning model that can predict water quality in various locations. The model takes into account several input parameters such as pH levels, conductivity, and chlorine. By analyzing these parameters, the system predicts the quality of water in terms of its suitability for different purposes, such as drinking, irrigation, or aquatic life.

The project involves the following steps:

1. Data Collection: The team gathered water quality data from various sources. The dataset includes historical water quality measurements along with corresponding location information.

2. Data Preprocessing: The collected data was cleaned and preprocessed to remove any inconsistencies or missing values. Feature engineering techniques were applied to extract relevant information and create meaningful features for the machine learning model.

3. Model Development: The team developed a machine learning model using Python. The model was trained on the preprocessed dataset, using machine learning algorithms and techniques for water quality prediction.

4. Model Evaluation: The trained model was evaluated using suitable evaluation metrics to measure its performance and accuracy. Cross-validation techniques were applied to ensure the model's reliability and generalizability.

5. Streamlit Integration: The Streamlit framework was utilized to create an interactive user interface for the water quality prediction system. The interface allows users to input the relevant parameters for a specific location and obtain the predicted water quality result.


## Requirements

To run the water quality prediction system locally, you need to have the following dependencies installed:

- Python 3.7 or above
- Streamlit
- scikit-learn
- TensorFlow

You can install the necessary Python packages by running the following command:

```shell
pip install -r requirements.txt
```

## Run Web Application Locally

To start the water quality prediction system, run the following command in your terminal:

```shell
streamlit run main.py
```

Once the application is running, you can access it through your web browser. The user interface will prompt you to input the relevant parameters such as pH levels, temperature, conductivity, and dissolved oxygen. After providing the required inputs, click the "Predict Water Quality" button to obtain the predicted water quality result for the specified location.


## Acknowledgments

I would like to acknowledge Omdena's Rwanda Chapter for providing the opportunity to work on this project. I also extend my gratitude to all the contributors who participated in developing and improving the water quality prediction system.