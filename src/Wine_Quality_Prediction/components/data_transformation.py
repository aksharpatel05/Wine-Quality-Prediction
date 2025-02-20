import os
from src.Wine_Quality_Prediction import logger
from sklearn.model_selection import train_test_split
from src.Wine_Quality_Prediction.entity.config_entity import DataTransformationConfig
import pandas as pd

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        """
        Initializes the DataTransformation class with the given configuration.

        Args:
            config (DataTransformationConfig): Configuration object containing paths for data.
        """
        self.config = config  # Storing config object

    def train_test_spliting(self):
        """
        Reads the dataset, splits it into training and testing sets, and saves them as CSV files.
        """
        data = pd.read_csv(self.config.data_path)  # Load dataset from CSV file

        # Split the data into training (75%) and test (25%) sets
        train, test = train_test_split(data, test_size = 0.25, random_state= 42)

        # Save the split datasets into the specified directory
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        # Log the split operation details
        logger.info("Split data into training and test sets")
        logger.info(train.shape)  # Log training data shape
        logger.info(test.shape)   # Log testing data shape

        # Print train and test dataset shapes
        print(train.shape)
        print(test.shape)

