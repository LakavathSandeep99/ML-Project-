import logging
import os
from datetime import datetime 

LOG_FILE = f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log'
loges_path = os.path.join("logs",LOG_FILE)
os.makedirs(loges_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(loges_path,LOG_FILE)

logging.basicConfig(
    filename =LOG_FILE_PATH,
    format = '[%(asctime)s]  %(lineno)d -%(levelname)s %(message)s',
    level = logging.INFO,

)

