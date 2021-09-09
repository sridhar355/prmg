FROM python:3.7-alpine

COPY *.py /tmp/

WORKDIR /tmp

CMD [ "python", "sample.py"]
