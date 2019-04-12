FROM python:3.6

COPY requirements.txt /app/

RUN pip install -r /app/requirements.txt

COPY . /app/

ENTRYPOINT "/app/entrypoint.sh"
