FROM python:3.12.2

ENV APP_HOME /app
ENV PYTHONUNBUFFERED 1



RUN pip install poetry

WORKDIR $APP_HOME

COPY ../../ .

# RUN poetry export -f requirements.txt > requirements.txt
RUN poetry install
