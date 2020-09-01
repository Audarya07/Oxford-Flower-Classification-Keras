FROM ubuntu:16.04

MAINTAINER Audarya Uttarwar <audiuttarwar2000@gmail.com>

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install opencv-python

RUN pip3 install keras

RUN apt-get install  -y libgtk2.0-dev  
ADD requirements.txt /
RUN pip3 install -r requirements.txt

COPY inference.py /
COPY model.h5 /
COPY imagelabels.mat /
COPY setid.mat /
COPY jpg / jpg/
COPY requirements.txt /

CMD ["python3", "./inference.py"]
