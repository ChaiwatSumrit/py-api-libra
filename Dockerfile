FROM python:3.6-alpine

RUN pip3 install pylibra flask flask-jsonpify flask-sqlalchemy flask-restful

ADD . /opt/api/
WORKDIR /opt/api
EXPOSE 8080
CMD ["python", "py-app.py"]