from python:3.11-alpine

WORKDIR /app

COPY requirements.txt /app
RUN pip install -U pip
RUN pip install -r requirements.txt
COPY . /app

CMD python3 -m uvicorn config.asgi:application --host 0.0.0.0 --port 8001
