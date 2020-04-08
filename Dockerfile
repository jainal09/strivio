FROM jainal09/strivio:latest
ENV PYTHONUNBUFFERED 1
RUN mkdir /strivio
WORKDIR /strivio
ADD . /strivio/
RUN chmod +x /strivio/run.sh
RUN python3 --version
CMD /strivio/run.sh
