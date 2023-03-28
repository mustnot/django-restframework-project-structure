FROM python:3.9-slim-bullseye

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

WORKDIR /app/django

RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc


COPY Pipfile Pipfile.lock /app/django/
RUN pipenv install --system --dev --ignore-pipfile

COPY . .

EXPOSE 8000
