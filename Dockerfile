FROM python:3
LABEL key="platzigram" 

ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY . /app/
RUN pip3 install -r requirements.txt

CMD python manage.py runserver 0.0.0.0:$PORT