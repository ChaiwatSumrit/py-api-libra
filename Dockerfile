# FROM python:3.6-alpine
FROM python:3.6-slim

COPY requirements.txt /app
COPY py-app.py /app
RUN pip install -r requirements.txt

EXPOSE 8080
CMD ["python", "py-app.py"]