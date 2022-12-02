from src.flows.covid_scraper.flow import track_covid_data 
from prefect.orion.schemas.schedules import CronSchedule
from prefect.deployments import Deployment
from src.config.blocks.s3_block import get_s3_bucket

class CRON_SCHEDULES:
    AT_3_PM_EACH_DAY = "0 15 * * *"

class TZ:
    INDIA="Asia/Kolkata"

class WORK_QUEUE:
    PROD_QUEUE = "prod_queue_1"

class FLOW_NAMES:
    COVID_TRACKER = "covid-tracker"

def main():
    covid_tracker_deployment_cron = Deployment.build_from_flow(
        flow=track_covid_data,
        name=FLOW_NAMES.COVID_TRACKER,
        storage=get_s3_bucket(),
        work_queue_name=WORK_QUEUE.PROD_QUEUE,
        schedule=(CronSchedule(cron=CRON_SCHEDULES.AT_3_PM_EACH_DAY, timezone=TZ.INDIA))
    )
    covid_tracker_deployment_cron.apply()

if __name__ == "__main__":
    main()