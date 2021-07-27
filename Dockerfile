FROM python:3-alpine

COPY . /project

WORKDIR /project

RUN  pip install -r requiremnts.txt

ENTRYPOINT ["python", "main.py"]