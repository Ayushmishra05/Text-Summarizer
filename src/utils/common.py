import yaml 
from box import ConfigBox
from pathlib import Path 
import os 
from ensure import ensure_annotations 
import sys 
from src.logging import logger 
from box.exceptions import BoxValueError


@ensure_annotations
def read_yaml(file_path : str):
    try:
        with open(file_path , 'r') as fp:
            data = yaml.safe_load(fp)
        return ConfigBox(data)
    except Exception as e:
        raise e 
    
    

@ensure_annotations
def create_dirs(path : str):
    try:
        dirname =os.path.dirname(path)
        os.makedirs(dirname , exist_ok= True)
    except Exception as e:
        raise e 
