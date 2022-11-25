
FROM python:3.9

WORKDIR /src

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false


# Copy using poetry.lock* in case it doesn't exist yet
COPY ./src/pyproject.toml ./src/poetry.lock* /src/

RUN poetry install --no-root --no-dev

COPY ./src /src


CMD ["uvicorn", "games.main:app", "--reload", "--host", "0.0.0.0", "--port", "80"]
