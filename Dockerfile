FROM mcr.microsoft.com/devcontainers/python:1-3.11-bullseye

WORKDIR /app

COPY requrements.txt .

RUN pip install --upgrade pip \
    && pip install --user -r requirements.txt \
    && playwright install chromium \
    && playwright install-deps

COPY . /app

WORKDIR /app/flat_scraper_project/

# CMD ["scrapy", "crawl", "apartments"]