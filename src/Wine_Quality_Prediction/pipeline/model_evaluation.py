from src.Wine_Quality_Prediction.config.configuration import ConfigurationManager
from src.Wine_Quality_Prediction.components.model_evaluation import ModelEvaluation
from src.Wine_Quality_Prediction import logger

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def initiate_model_evaluation(self): 
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Starting {STAGE_NAME} <<<<<<<<")
        obj = ModelEvaluationPipeline()
        obj.initiate_model_evaluation()
        logger.info(f">>>>>> Finished {STAGE_NAME} <<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e