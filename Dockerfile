# pull official base image
FROM python:3.11.1-alpine
LABEL maintainer="alisher.khalikulov"

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


COPY ./scripts /scripts
COPY ./app/requirements.txt /requirements.txt
COPY ./app /app

# set work directory
WORKDIR /app

# install dependencies
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps \
        build-base postgresql-dev musl-dev linux-headers gcc python3-dev && \
    /py/bin/pip install -r /requirements.txt && \
    apk del .tmp-deps && \
    adduser --disabled-password --no-create-home app && \
    chmod -R +x /scripts


# environ
ENV PATH="/scripts:/py/bin:$PATH"

USER app

