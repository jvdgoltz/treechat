FROM python:3.11

ENV PORT=8000
ENV GUNICORN_WORKERS=4

COPY . /app
WORKDIR /app

RUN pip install .


ENV GUNICORN_CMD_ARGS="--bind=0.0.0.0:$PORT --workers=$GUNICORN_WORKERS"

ENTRYPOINT ["gunicorn", "app:app"]