FROM python:3

COPY sample.py /tmp/

WORKDIR /tmp

CMD [ "python", "sample.py"]
