FROM python:3.6-slim-buster

#COPY ./requirements.txt .
COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

#COPY . .
EXPOSE 5000

CMD [ "python", "app.py" ]
#CMD [ "flask", "run", "--host=0.0.0.0", "--port=80" ]