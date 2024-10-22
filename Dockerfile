# syntax=docker/dockerfile:1
FROM python:3.12.7-slim-bookworm
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
