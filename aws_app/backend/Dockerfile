FROM python:3.9-slim-buster

WORKDIR /backend

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8081

COPY . .

CMD ["gunicorn", "wsgi:app", "-w 2", "-b 0.0.0.0:8081", "-t 30"]