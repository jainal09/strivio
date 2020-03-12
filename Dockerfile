# The first instruction is what image we want to base our container on
# We Use an official ubuntu 18.04
FROM ubuntu:18.04
FROM python:3.7

RUN apt-get update \
  && apt-get install -y python3.7-dev \
  && apt-get install -y python3-pip \
  && pip3 install --upgrade pip
# Install GCC client
RUN apt-get -y install gcc

# Install G++
RUN apt-get -y install g++

#Install jdk
RUN apt-get -y install default-jdk

# Define working directory.

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

## create root directory for our project in the container
RUN mkdir /strivio
#
## Set the working directory to /mpi_video_tools
WORKDIR /strivio
#
## Copy the current directory contents into the container at /strivio
ADD . /strivio/
RUN echo "drop"
RUN echo $drop
CMD echo "drop" >> /strivio/yaml_files/dropbox_uploader.conf
RUN chmod +x /strivio/yaml_files/dropbox_uploader.sh
RUN  /strivio/yaml_files/dropbox_uploader.sh -f \
  /strivio/yaml_files/dropbox_uploader.conf download IO.yaml ./yaml_files/IO.yaml

## Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt
CMD python3 /strivio/Evaluater/Evaluate.py
