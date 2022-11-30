from src.flows.covid_scraper.flow import track_covid_data 
from prefect.orion.schemas.schedules import CronSchedule
from prefect.deployments import Deployment

class CRON_SCHEDULES:
    AT_3_PM_EACH_DAY = "0 15 * * *"

class TZ:
    INDIA="Asia/Kolkata"

covid_tracker_deployment_cron = Deployment.build_from_flow(
    flow=track_covid_data,
    name="covid-tracker",
    work_queue_name="test",
    schedule=(CronSchedule(cron=CRON_SCHEDULES.AT_3_PM_EACH_DAY, timezone=TZ.INDIA))
)

if __name__ == "__main__":
    covid_tracker_deployment_cron.apply()