FROM python:3.9.0b4-alpine3.12

WORKDIR /usr/src/app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apk update \
    && apk add gcc g++ musl-dev libc-dev bash \
    && apk add python3-dev postgresql postgresql-dev \
    && apk add libffi-dev libxml2 libffi-dev \
    && apk add jpeg-dev zlib-dev libjpeg
ENV PATH="/bin/bash:${PATH}"

COPY ./requirements.txt .
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
