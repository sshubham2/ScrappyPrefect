from dotenv import dotenv_values
from unipath import Path
import os

class ENV_VARS():
    COVID_SCRAPE_URL = 'COVID_SCRAPE_URL'
    AWS_SECRET_ACCESS_KEY = 'AWS_SECRET_ACCESS_KEY'
    AWS_ACCESS_KEY_ID = 'AWS_ACCESS_KEY_ID'

def getPath():
    path = Path( os.path.dirname(os.path.abspath(__file__)))
    p = path.parent.parent + "/environment/.env"
    return p

def load_settings():
    return dotenv_values(getPath())

settings = load_settings()
