import firebase_admin, os
from firebase_admin import credentials
from firebase_admin import firestore
from unipath import Path

class COLLECTIONS:
    COVID_RECORDS = "covid-records"
    
def getPath():
    path = Path( os.path.dirname(os.path.abspath(__file__)))
    p = path.parent.parent + "/environment/serviceAccount.json"
    return p

cred = credentials.Certificate(getPath())
app = firebase_admin.initialize_app(cred)
db = firestore.client()
