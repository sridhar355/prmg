FROM python:3

ADD my_script.py /

CMD [ "python", "./dict.py" ]
