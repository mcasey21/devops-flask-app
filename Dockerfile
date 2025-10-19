FROM python:3.11-slim

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip Flask

EXPOSE 5000

CMD ["python", "hello.py"]

