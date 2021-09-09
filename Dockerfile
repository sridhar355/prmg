FROM python:3.7-alpine

COPY sample.py /tmp/

WORKDIR /tmp

CMD [ "python", "sample.py"]
