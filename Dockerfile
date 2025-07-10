FROM python:3.13.5-alpine

# Установка chromium и системных зависимостей (без chromium-chromedriver)
RUN apk update && \
    apk add --no-cache chromium openjdk11-jre tzdata curl tar gcc musl-dev libffi-dev python3-dev && \
    chromium --version # Проверка версии Chromium

# Установка Allure Command Line
RUN curl -o allure-2.34.1.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.34.1/allure-commandline-2.34.1.tgz && \
    tar -zxvf allure-2.34.1.tgz -C /opt/ && \
    ln -s /opt/allure-2.34.1/bin/allure /usr/bin/allure && \
    rm allure-2.34.1.tgz

# Установка рабочей директории
WORKDIR /usr/workspace

# Копирование requirements.txt и установка Python-зависимостей
COPY ./requirements.txt /usr/workspace

# Копирование проекта
COPY . /usr/workspace

# Очистка кэша apk
RUN rm -rf /var/cache/apk/*