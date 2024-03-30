FROM python:3.9-slim-buster

WORKDIR /APP

COPY requirement.txt requirement.txt

RUN pip install -r requirement.txt

COPY . . 

EXPOSE 8000

CMD python manage.py runserver

