FROM python:3.7

COPY ./requirements.txt ./

RUN pip3 install -r requirements.txt

COPY src/main.py ./main.py
COPY src/getcontact ./getcontact
COPY dump/tokens.yaml ./dump/tokens.yaml
COPY src/flask .

ENTRYPOINT ["python3"]
CMD ["./app.py"]
