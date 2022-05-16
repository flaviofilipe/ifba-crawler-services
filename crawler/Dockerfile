FROM python:3.9-alpine
RUN apk update 
RUN mkdir /usr/src/app
WORKDIR /usr/src/app
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt
RUN pip freeze
COPY . .