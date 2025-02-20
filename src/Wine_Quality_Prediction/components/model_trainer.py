import os
import pandas as pd
import joblib
from sklearn.linear_model import ElasticNet
from src.Wine_Quality_Prediction import logger
from src.Wine_Quality_Prediction.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        """
        Initializes the ModelTrainer class with configuration settings.

        Args:
            config (ModelTrainerConfig): Configuration object that contains paths 
                                         and model hyperparameters.
        """
        self.config = config  # Store the configuration object

    def train(self):
        """
        Trains an ElasticNet regression model using the provided dataset and saves the trained model.
        """

        # Load Training and Testing Data
        train_data = pd.read_csv(self.config.train_data_path)  # Load training dataset
        test_data = pd.read_csv(self.config.test_data_path)    # Load testing dataset

        # Separate Features and Target Variable
        # Drop the target column to get only features (X)
        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)

        # Extract only the target column (y)
        train_y = train_data[[self.config.target_column]]
        test_y = test_data[[self.config.target_column]]

        # Initialize the Model
        lr = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42)

        # Train the Model
        lr.fit(train_x, train_y)

        # Save the Trained Model
        joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))

        logger.info(f"Model training complete. Model saved as {self.config.model_name}.")
