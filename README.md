Prerequisites
1. Login to prefect.io
2. Ask workspace access and queue_name.
3. Create prefect API key.
4. pip install -U prefect
5. run - ```prefect cloud login --key < apikey > --workspace < workspacename >```

To Deploy flows on S3:
1. After cloning repo, Ask for /environment .env and serviceAccount.json files and copy to /environment folder in local repo.
2. run ```pip install requirements.txt```
3. run ```python deployment.py```

To run agent:
1. In local machine, go to repo then run:
```
docker build \
-f agent.Dockerfile \
--build-arg prefect_key=< apiKey > \
--build-arg work_space=< workspacename > \
--build-arg work_queue=< queue_name > \
-t prefect-agent .
```
   
2. Then, run: 
```
docker run -it prefect-agent
```
Execute on_demand tasks by going to prefect.io workspace.
