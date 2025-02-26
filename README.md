# Wine Quality Prediction

This project aims to predict the quality of wine based on various chemical properties using machine learning techniques. The project follows an MLOps approach to ensure reproducibility, scalability, and maintainability.

## Project Overview

The goal of this project is to build a machine learning model that can predict the quality of wine based on its chemical properties. The project involves data ingestion, validation, transformation, model training, and evaluation. Additionally, a web application is provided to allow users to input wine properties and get a predicted quality score.

## Tech Stack

- **Programming Language**: Python
- **Web Framework**: Flask
- **Machine Learning**: Scikit-learn, Pandas, NumPy
- **Data Visualization**: Matplotlib, Seaborn
- **MLOps**: MLflow, DagsHub
- **Version Control**: Git


## Project Pipelines

The project consists of the following pipelines:

1. **Data Ingestion**: Downloads and extracts the dataset.
2. **Data Validation**: Validates the dataset against the schema.
3. **Data Transformation**: Splits the dataset into training and testing sets.
4. **Model Training**: Trains an ElasticNet regression model.
5. **Model Evaluation**: Evaluates the trained model and logs metrics to MLflow.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/aksharpatel05/Wine_Quality_Prediction.git
    cd Wine_Quality_Prediction
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

Update the configuration files as needed:

- [config.yaml](http://_vscodecontentref_/9): Contains paths and URLs for data ingestion, validation, transformation, model training, and evaluation.
- [params.yaml](http://_vscodecontentref_/10): Contains hyperparameters for the model.
- [schema.yaml](http://_vscodecontentref_/11): Defines the schema for the dataset.

## Running the Project

1. To train the model, run:
    ```sh
    python main.py
    ```

2. To start the Flask web application, run:
    ```sh
    python app.py
    ```






