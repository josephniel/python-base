FROM node:latest

MAINTAINER Joseph Niel Tuazon

ADD . /app
WORKDIR /app

RUN npm install webpack babel -g
RUN npm install

CMD webpack -d --watch --config webpack/webpack.config.js
