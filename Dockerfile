FROM ubuntu:latest

RUN apt update && apt install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get install -y python3.8-dev python3-pip libsm6 libxext6 build-essential ffmpeg libsm6 libxext6 tesseract-ocr

RUN pip3 install pillow
RUN pip3 install pytesseract
RUN pip3 install opencv-contrib-python


# Copy project
COPY ./ ./

RUN pip3 install -r requirements.txt


ENTRYPOINT ["./run.sh"]
CMD []
