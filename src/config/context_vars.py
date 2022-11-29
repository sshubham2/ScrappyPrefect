from dotenv import dotenv_values
from unipath import Path
import os

class ENV_VARS():
    COVID_SCRAPE_URL = 'COVID_SCRAPE_URL'

def getPath():
    path = Path( os.path.dirname(os.path.abspath(__file__)))
    p = path.parent.parent + "/environment/.env"
    return p

def load_settings():
    return dotenv_values(getPath())

settings = load_settings()
