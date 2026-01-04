FROM python:3.11

ENV PORT=8000

COPY . /app
WORKDIR /app

RUN pip install .

CMD ["gunicorn", "--bind", "0.0.0.0:${PORT}", "app:app"]