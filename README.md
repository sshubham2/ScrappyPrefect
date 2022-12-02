To Deploy flows on S3:
1. After cloning repo, Ask for /environment .env and serviceAccount.json files and copy to /environment folder in local repo.
2. pip install requirements.txt
3. run python deployment.py

To run agent:
1. Login to prefect.io
2. Ask workspace access.
3. Create prefect API key.
4. In local machine, prefect cloud login -k < keyname > --workspace < workspacename >
5. Then, run prefect agent start -q <queue_name>
6. Run tasks by going to prefect.io workspace.
