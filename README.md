-Prerequisites
1. Login to prefect.io
2. Ask workspace access and queue_name.
3. Create prefect API key.

-To Deploy flows on S3:
1. After cloning repo, Ask for /environment .env and serviceAccount.json files and copy to /environment folder in local repo.
2. run ```pip install requirements.txt```
3. run - ```prefect cloud login --key < apikey > --workspace < workspacename >```
4. run ```python deployment.py```

-To run agent:
1. In local machine, go to repo then run:
```docker build -f agent.Dockerfile -t prefect-agent .```
   
2. Then, run: 
```docker run -it prefect-agent <apiKey> <workspaceName> <queueName>```

Execute on_demand tasks by going to prefect.io workspace.
