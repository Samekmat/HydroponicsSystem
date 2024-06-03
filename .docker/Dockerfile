FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && \
    apk add --no-cache \
    postgresql-dev \
    gcc \
    musl-dev \
    postgresql-client

WORKDIR /code

RUN pip install poetry

COPY ../pyproject.toml ../poetry.lock /code/
RUN poetry install --no-root --no-interaction

COPY ../ /code/

EXPOSE 8000

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
