FROM python:3.7-alpine

COPY *.py /temp/sample.py

WORKDIR /temp

CMD [ "python", "sample.py"]
