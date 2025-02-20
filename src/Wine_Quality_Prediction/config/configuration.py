from src.Wine_Quality_Prediction.constants import * #import constant file paths
from src.Wine_Quality_Prediction.utils.common import read_yaml, create_directories #import helper functions
from src.Wine_Quality_Prediction.entity.config_entity import (DataIngestionconfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig, ModelEvaluationConfig) #import config entity classes
import os
from dotenv import load_dotenv

class ConfigurationManager:
    def __init__(self,
                 config_filepath = CONFIG_FILE_PATH,
                 params_filepath = PARAMS_FILE_PATH,
                 schema_filepath = SCHEMA_FILE_PATH):
        
        #Reads configuration files
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        # Creates artifacts_root directory, where all pipeline outputs will be stored.
        create_directories([self.config.artifacts_root])

    #Data Ingestion Configuration
    def get_data_ingestion_config(self)-> DataIngestionconfig:
        config = self.config.data_ingestion # Access data ingestion configuration
        create_directories([config.root_dir]) ## Ensure the ingestion directory exists

        #Creates an instance of DataIngestionconfig with values from config.yaml
        data_ingestion_config = DataIngestionconfig(
            root_dir = config.root_dir,
            source_URL= config.source_URL,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir)
        
        #Returns the configured data ingestion object.
        return data_ingestion_config

    #Data Validation Configuration
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir = config.unzip_data_dir,
            all_schema=schema,
        )

        return data_validation_config

    #Data Tranasformation Configuration
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
        )

        return data_transformation_config

    #Model Trainer Configuration
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.ElasticNet
        schema =  self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path = config.train_data_path,
            test_data_path = config.test_data_path,
            model_name = config.model_name,
            alpha = params.alpha,
            l1_ratio = params.l1_ratio,
            target_column = schema.name
            
        )

        return model_trainer_config

    #Model Evaluation Configuration
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        """
        Retrieves the configuration required for model evaluation.

        Returns:
        - ModelEvaluationConfig object containing paths and evaluation parameters.
        """
        # Extract evaluation-related configurations
        config = self.config.model_evaluation  # Get model evaluation settings
        params = self.params.ElasticNet  # Get ElasticNet hyperparameters
        schema = self.schema.TARGET_COLUMN  # Get target column name

        # Ensure the evaluation directory exists
        create_directories([config.root_dir])

        # Create a structured ModelEvaluationConfig object
        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,  # Directory for evaluation artifacts
            test_data_path=config.test_data_path,  # Path to test dataset
            model_path=config.model_path,  # Path to the trained model
            all_params=params,  # ML model parameters from params.yaml
            metric_file_name=config.metric_file_name,  # Name of the metric file
            target_column=schema.name,  # Target column for evaluation
            mlflow_uri=os.environ.get("MLFLOW_TRACKING_URI")  # MLflow tracking URI
        )

        return model_evaluation_config  # Return the structured config object
