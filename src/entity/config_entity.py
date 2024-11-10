from dataclasses import dataclass
@dataclass 
class DataIngestionConfig:
    ingestion_root : str 
    data_path : str 
    zip_dir : str 
    unzip_local_dir : str 