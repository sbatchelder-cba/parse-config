FROM python:3.12-alpine3.19

RUN apk add yq
RUN pip install pyyaml

RUN mkdir /tools
COPY ./parse_config.py /tools/parse_config.py
COPY ./validate_config.py /tools/validate_config.py