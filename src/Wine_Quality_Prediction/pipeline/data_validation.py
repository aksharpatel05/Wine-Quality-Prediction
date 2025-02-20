from src.Wine_Quality_Prediction.config.configuration import ConfigurationManager
from src.Wine_Quality_Prediction.components.data_validation import DataValiadtion
from src.Wine_Quality_Prediction import logger

STAGE_NAME = "Data Validation Stage"

class DataValidationPipeline:
    def __init__(self):
        pass
    
    def initiate_data_validation(self): 
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_columns()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Starting {STAGE_NAME} <<<<<<<<")
        obj = DataValidationPipeline()
        obj.initiate_data_validation()
        logger.info(f">>>>>> Finished {STAGE_NAME} <<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e