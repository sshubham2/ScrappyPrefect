import prefect
from lxml import html
from datetime import datetime
import requests
import pandas as pd
from src.config.firestore import db, COLLECTIONS
from src.config.context_vars import settings, ENV_VARS
from src.flows.covid_scraper.utils import *

@prefect.task()
def get_india_covid_date(_url: str):
   tree = html.fromstring(requests.get(_url).content)
   _date = ''.join(tree.xpath(XpathQ.DATE)[0].split()[3:7]).replace(',', '')+'+05:30'
   return pd.DataFrame({
      'timestamp': [datetime.strptime(_date, DATE_FORMAT).isoformat()], 
      'total_active_cases': [int(tree.xpath(XpathQ.ACTIVE_CASE)[0].strip())], 
      'total_discharged': [int(''.join(tree.xpath(XpathQ.TOTAL_DISCHARGED)).strip())],
      'total_vaccination': [int(''.join(tree.xpath(XpathQ.TOTAL_DEATHS)).strip())], 
      'total_deaths': [int(''.join(tree.xpath(XpathQ.TOTAL_VACC)).strip().replace(',', ''))]
   })

@prefect.task()
def load_data(df: pd.DataFrame):
   records = df.to_dict('records')
   for record in records:
      db.collection(COLLECTIONS.COVID_RECORDS).add(record)

@prefect.flow()
def main():
   df = get_india_covid_date(settings[ENV_VARS.COVID_SCRAPE_URL])
   load_data(df)
   
if __name__ == '__main__':    
    main()

