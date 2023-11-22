FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

RUN pip install django-cors-headers

RUN poetry add gunicorn

COPY . /app/

EXPOSE 8000

RUN poetry run python manage.py collectstatic --noinput --clear

CMD ["poetry", "run", "gunicorn", "vin.wsgi:application", "--bind", "0.0.0.0:8000"]
