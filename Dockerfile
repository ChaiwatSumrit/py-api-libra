# FROM python:3.6-alpine
FROM python:3.6-slim

COPY . /usr/src/app

RUN pip3 install pylibra flask flask-jsonpify flask-sqlalchemy flask-restful
WORKDIR /usr/src/app
EXPOSE 3000
CMD ["python3", "py-app.py"]
