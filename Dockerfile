FROM python:3.13.5-alpine3.20
# install chromedriver
RUN apk update
RUN apk add --no-cache chromium chromium-chromedriver tzdata

# Get all the prereqs
RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub
RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.35-r1/glibc-2.35-r1.apk
RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.35-r1/glibc-bin-2.35-r1.apk

RUN apk update && \
    apk add openjdk11-jre curl tar && \
    curl -o allure-2.34.1.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.34.1/allure-commandline-2.34.1.tgz && \
    tar -zxvf allure-2.34.1.tgz -C /opt/ && \
    ln -s /opt/allure-2.34.1/bin/allure /usr/bin/allure && \
    rm allure-2.34.1.tgz

WORKDIR /usr/workspace

# Copy the dependencies file to the working directory
COPY ./requirements.txt /usr/workspace

# Install Python dependencies
RUN pip3 install -r requirements.txt