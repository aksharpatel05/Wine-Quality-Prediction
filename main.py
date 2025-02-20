from src.Wine_Quality_Prediction import logger
from src.Wine_Quality_Prediction.pipeline.data_ingestion import DataIngestionTrainingPipeline
from src.Wine_Quality_Prediction.pipeline.data_validation import DataValidationPipeline
from src.Wine_Quality_Prediction.pipeline.data_transformation import DataTransformationPipeline
from src.Wine_Quality_Prediction.pipeline.model_trainer import ModelTrainerPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> Starting {STAGE_NAME} <<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()
    logger.info(f">>>>>> Finished {STAGE_NAME} <<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>>> Starting {STAGE_NAME} <<<<<<<<")
    obj = DataValidationPipeline()
    obj.initiate_data_validation()
    logger.info(f">>>>>> Finished {STAGE_NAME} <<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f">>>>>> Starting {STAGE_NAME} <<<<<<<<")
    obj = DataTransformationPipeline()
    obj.initiate_data_transformation()
    logger.info(f">>>>>> Finished {STAGE_NAME} <<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Trainer Stage"

try:
    logger.info(f">>>>>> Starting {STAGE_NAME} <<<<<<<<")
    obj = ModelTrainerPipeline()
    obj.initiate_model_trainer()
    logger.info(f">>>>>> Finished {STAGE_NAME} <<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e