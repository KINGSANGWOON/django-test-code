FROM python:3.7

ENV PYTHONUMBUFFERED 1

WORKDIR /app

COPY . .

EXPOSE 80

RUN pip3 install -r requirements.txt

CMD python3 manage.py runserver 0.0.0.0:80
