FROM python:3.13.5-alpine

# Install system dependencies
RUN apk update && \
    apk add --no-cache \
        chromium \
        chromium-chromedriver \
        tzdata \
        openjdk11-jre \
        curl \
        tar

# Install Allure CLI
RUN curl -o allure-2.34.1.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.34.1/allure-commandline-2.34.1.tgz && \
    tar -zxvf allure-2.34.1.tgz -C /opt/ && \
    ln -s /opt/allure-2.34.1/bin/allure /usr/bin/allure && \
    rm allure-2.34.1.tgz

# Set working directory
WORKDIR /usr/workspace

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .