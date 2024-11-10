from src.components.data_ingestion import DataIngestion 
from src.config.configuration import ConfigurationMananger 
from src.entity.config_entity import DataIngestionConfig 




config = ConfigurationMananger()
files = config.data_ingestion()
ingestion = DataIngestion(files)
ingestion.initiate_data_ingestion()
