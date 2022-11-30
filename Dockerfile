FROM prefecthq/prefect:latest-python3.9
ARG prefect_secret
ARG workspace

RUN apt update -y
RUN apt install -y gcc libpq-dev python3-dev liblzma-dev

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
RUN prefect cloud login --key ${prefect_secret} --workspace ${workspace}

COPY . /prefect-flows
WORKDIR /prefect-flows

ENV PYTHONPATH=/prefect-flows
CMD ["python", "deployment.py", "&&", "prefect", "agent", "start", "-q", "test"]