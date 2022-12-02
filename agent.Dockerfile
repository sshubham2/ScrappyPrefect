FROM ubuntu:latest

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y
RUN apt-get install -y python3 python3-pip

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY run_agent.sh .
RUN chmod +x run_agent.sh

ENTRYPOINT [ "./run_agent.sh" ]



