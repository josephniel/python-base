FROM python:3.6

ADD . /app
WORKDIR /app

RUN pip install -e .

EXPOSE 5000

CMD ["python3", "app.py"]