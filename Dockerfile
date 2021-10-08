FROM python:3.9-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY  . /code
RUN pip install -r ./requirements/requirements.txt
WORKDIR /code
