import os
import urllib.request as request
from src.Wine_Quality_Prediction import logger
import zipfile
from src.Wine_Quality_Prediction.entity.config_entity import DataIngestionconfig

class DataIngestion:
    def __init__(self, config: DataIngestionconfig):
        self.config = config # Stores the configuration parameters

    #downloading the zip file
    def download_file(self):
        if not os.path.exists(self.config.local_data_file): ## Check if file already exists
            filename, headers = request.urlretrieve(
                self.config.source_URL,
                self.config.local_data_file
            )  # Download the file
            logger.info(f"{filename} downloaded! with following info: \n{headers}" ) 
        else:
            logger.info(f"File already exists")


        #extract the zip file
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)