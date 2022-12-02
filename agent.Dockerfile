FROM ubuntu:latest

ARG prefect_key
ARG work_space
ARG work_queue

ENV DEBIAN_FRONTEND noninteractive
ENV WORK_QUEUE ${work_queue}

RUN apt-get update -y
RUN apt-get install -y python3 python3-pip

COPY requirements.txt .
RUN pip install -r requirements.txt


RUN prefect cloud login --key ${prefect_key} --workspace ${work_space}
CMD prefect agent start -q ${WORK_QUEUE}



