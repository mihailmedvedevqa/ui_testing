FROM python:3.13.5-alpine

# Установка chromedriver и системных зависимостей
RUN apk update && \
    apk add --no-cache chromium chromium-chromedriver openjdk11-jre tzdata curl tar gcc musl-dev libffi-dev python3-dev

# Установка Allure Command Line
RUN curl -o allure-2.34.1.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.34.1/allure-commandline-2.34.1.tgz && \
    tar -zxvf allure-2.34.1.tgz -C /opt/ && \
    ln -s /opt/allure-2.34.1/bin/allure /usr/bin/allure && \
    rm allure-2.34.1.tgz

# Установка рабочей директории
WORKDIR /usr/workspace

# Копирование requirements.txt и проверка его наличия
COPY ./requirements.txt /usr/workspace/requirements.txt
RUN ls -la /usr/workspace/requirements.txt && \
    cat /usr/workspace/requirements.txt && \
    pip3 install --no-cache-dir -r /usr/workspace/requirements.txt && \
    pip3 show pytest # Проверка установки pytest

# Копирование проекта
COPY . /usr/workspace

# Очистка кэша apk
RUN rm -rf /var/cache/apk/*