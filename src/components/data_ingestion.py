from src.config.configuration import DataIngestionConfig
from urllib.request import urlretrieve
from zipfile import ZipFile
class DataIngestion:
    def __init__(self,  data_ingestion_config : DataIngestionConfig):
        self.config = data_ingestion_config
    
    def initiate_data_ingestion(self):
        try:
            data = urlretrieve(self.config.data_path, self.config.zip_dir)
            with ZipFile(self.config.zip_dir, 'r') as zo:
                zo.extractall(self.config.unzip_local_dir)
        except Exception as e:
            raise e

    