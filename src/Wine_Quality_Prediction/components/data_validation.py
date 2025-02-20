import os
import pandas as pd
from src.Wine_Quality_Prediction import logger
from src.Wine_Quality_Prediction.entity.config_entity import DataValidationConfig


class DataValiadtion:
    def __init__(self, config: DataValidationConfig):
        """Initialize the DataValidation component with the given configuration."""
        self.config = config

    def validate_all_columns(self)-> bool:
        """Validates if the dataset contains all required columns."""
        try:
            validation_status = None

            # Load the dataset
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)  # Extract column names from the dataset

            all_schema = self.config.all_schema.keys() # Expected columns from the schema file

            # Check if all columns exist in the schema
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False # Set status to False if any column is missing
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}") # Save status in file
                else:
                    validation_status = True # If column exists, mark as valid
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

            return validation_status  # Return final validation status
        
        except Exception as e:
            raise e  # Raise exception if any error occurs
