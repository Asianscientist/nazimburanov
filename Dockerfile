# Use an official Python runtime as the base image
FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1
ENV PIP_NO_CACHE_DIR=off

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
