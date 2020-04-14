FROM jainal09/strivio:latest
WORKDIR /strivio
ADD . /strivio/
RUN chmod +x /strivio/run.sh
CMD /strivio/run.sh
