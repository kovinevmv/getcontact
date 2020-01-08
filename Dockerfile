FROM python:3.7

COPY ./requirements.txt ./

RUN pip3 install -r requirements.txt

COPY src/main.py ./src/main.py
COPY src/getcontact ./src/getcontact
COPY dump/tokens.yaml ./dump/tokens.yaml
COPY ./run.sh ./run.sh

ENTRYPOINT [“bash”, “-c”, “chmod 777 ./run.sh”]
ENTRYPOINT ["./run.sh"]
CMD []
