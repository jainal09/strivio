FROM ubuntu:18.04
FROM python:3.7
FROM openjdk:7
RUN apt-get -y update && apt-get install -y python3-pip
ENV PYTHONUNBUFFERED 1
RUN mkdir /strivio
WORKDIR /strivio
ADD . /strivio/
RUN pip3 install -r requirements.txt
RUN chmod +x /strivio/run.sh
CMD /strivio/run.sh
