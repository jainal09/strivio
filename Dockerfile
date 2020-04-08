FROM sabbir1cse/ubuntu-python-pip-supervisor
ENV PYTHONUNBUFFERED 1
RUN mkdir /strivio
WORKDIR /strivio
ADD . /strivio/
RUN pip3 install -r requirements.txt
RUN chmod +x /strivio/run.sh
CMD /strivio/run.sh
