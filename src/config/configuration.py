from src.utils.common import create_dirs, read_yaml
from src.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from src.entity.config_entity import DataIngestionConfig
class ConfigurationMananger:
    def __init__(self, config_file_path =  CONFIG_FILE_PATH , params_file_path =  PARAMS_FILE_PATH):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        create_dirs(self.config.root_artifacts)
    
    def data_ingestion(self) -> DataIngestionConfig:
        create_dirs(self.config.data_ingestion.ingestion_root)
        create_dirs(self.config.data_ingestion.unzip_local_dir)
        create_dirs(self.config.data_ingestion.zip_dir)
        with open(self.config.data_ingestion.zip_dir , 'w') as fp:
            pass
        data_path = self.config.data_ingestion.data_path 


        return DataIngestionConfig(
            ingestion_root=self.config.data_ingestion.ingestion_root, 
            data_path = self.config.data_ingestion.data_path, 
            zip_dir = self.config.data_ingestion.zip_dir, 
            unzip_local_dir=self.config.data_ingestion.unzip_local_dir
        )
        
        