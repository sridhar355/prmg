FROM python:3.7-alpine

COPY *.py /tmp/sample.py

WORKDIR /tmp

CMD [ "python", "sample.py"]
