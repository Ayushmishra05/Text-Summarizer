import logging 
from datetime import datetime 
import logging.handlers
import os 
file_name = f"{datetime.now().strftime("%H_%M_%d_%m_%Y")}.log"
import sys

file_dir = f"logs/{file_name}"
direc = os.path.dirname(file_dir)
os.makedirs(direc , exist_ok= True)

logging.basicConfig(
    level=logging.INFO, 
    format=f"%(asctime)s - %(levelname)s - %(message)s", 
    handlers=[
        logging.FileHandler(file_dir), 
        logging.StreamHandler(sys.stdout)
    ]
)


logger = logging.getLogger("summarizer")