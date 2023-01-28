FROM  python:3.10

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN pip install --upgrade pip setuptools

WORKDIR /api-django
COPY requirements.txt .
RUN pip install -r requirements.txt
