FROM jenkins/jenkins:lts
USER root
RUN mkdir /pytest_app
WORKDIR /pytest_app
COPY requirements.txt /pytest_app
RUN pwd
RUN ls -la
RUN apt-get update
RUN apt-get install -y python3-pip
