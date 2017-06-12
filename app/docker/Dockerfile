FROM python:3.6

MAINTAINER Joseph Niel Tuazon

ADD . /app
WORKDIR /app

RUN pip install -e .

EXPOSE 5000

CMD ["python3", "__init__.py"]