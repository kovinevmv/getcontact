FROM ubuntu:latest

RUN apt-get update -y
# Install Python
RUN apt-get install -y python3-pip python3.7

# Install tesseract
RUN apt update && apt install -y libsm6 libxext6

RUN export DEBIAN_FRONTEND=noninteractive
RUN ln -fs /usr/share/zoneinfo/Europe/Moscow /etc/localtime
RUN apt-get install -y tzdata
RUN dpkg-reconfigure --frontend noninteractive tzdata

RUN apt-get -y install tesseract-ocr

# Install Python packages
COPY ./requirements.txt ./
RUN pip3 install -r requirements.txt

# Move src
COPY src/main.py ./src/main.py
COPY src/getcontact ./src/getcontact
COPY dump/tokens.yaml ./dump/tokens.yaml
COPY ./run.sh ./run.sh

# Support Emoji
ENV LANG C.UTF-8

# Set rights to executable
ENTRYPOINT [“bash”, “-c”, “chmod 777 ./run.sh”]
ENTRYPOINT ["./run.sh"]
CMD []
