#component
import os
import pandas as pd
from src.Wine_Quality_Prediction.utils.common import save_json, read_yaml, create_directories
from src.Wine_Quality_Prediction.entity.config_entity import ModelEvaluationConfig
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from pathlib import Path

from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Now, these variables will be set
os.environ["MLFLOW_TRACKING_URI"] = os.getenv("MLFLOW_TRACKING_URI")
os.environ["MLFLOW_TRACKING_USERNAME"] = os.getenv("MLFLOW_TRACKING_USERNAME")
os.environ["MLFLOW_TRACKING_PASSWORD"] = os.getenv("MLFLOW_TRACKING_PASSWORD")


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        """
        Initializes the ModelEvaluation class with a configuration object.
        
        Args:
            config (ModelEvaluationConfig): Contains all the necessary configuration
                                            parameters such as file paths, target column,
                                            MLflow URI, and model parameters.
        """
        self.config = config  # Store the configuration for later use

    def eval_metrics(self, actual, pred):
        """
        Computes evaluation metrics for the model predictions.
        
        Args:
            actual (array-like): The true target values.
            pred (array-like): The predicted target values from the model.
            
        Returns:
            tuple: Contains RMSE, MAE, and R2 score.
        """
        # Calculate Root Mean Squared Error (RMSE)
        rmse = np.sqrt(mean_squared_error(actual, pred))
        # Calculate Mean Absolute Error (MAE)
        mae = mean_absolute_error(actual, pred)
        # Calculate R-squared (R2) score
        r2 = r2_score(actual, pred)
        return rmse, mae, r2

    def log_into_mlflow(self):
        """
        Loads the test data and trained model, performs predictions,
        computes evaluation metrics, saves these metrics locally, logs parameters
        and metrics to MLflow, and finally logs the model into MLflow's model registry.
        """
        # Load test dataset from CSV using the path specified in the configuration
        test_data = pd.read_csv(self.config.test_data_path)
        # Load the trained model from file
        model = joblib.load(self.config.model_path)

        # Separate features (test_x) from target variable (test_y)
        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]

        # Set the MLflow registry URI to the one provided in the configuration
        mlflow.set_registry_uri(self.config.mlflow_uri)
        # Parse the MLflow tracking URI to determine its scheme (e.g., file, http)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        # Start an MLflow run to log metrics, parameters, and the model
        with mlflow.start_run():
            # Use the loaded model to predict target values for the test set
            predicted_qualities = model.predict(test_x)

            # Evaluate the model predictions using the defined eval_metrics function
            (rmse, mae, r2) = self.eval_metrics(test_y, predicted_qualities)
            
            # Save the evaluation metrics locally as a JSON file
            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            # Log all model parameters from the configuration to MLflow
            mlflow.log_params(self.config.all_params)

            # Log evaluation metrics to MLflow
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2", r2)

            # Check if the MLflow tracking store is not a local file system
            if tracking_url_type_store != "file":
                # If not, register the model with MLflow's Model Registry.
                # Registered model name is specified as "ElasticnetModel".
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticnetModel")
            else:
                # Otherwise, log the model without registry registration
                mlflow.sklearn.log_model(model, "model")
