FROM  207457565/flask:latest

COPY . /project

WORKDIR /project

# RUN  pip install -r requiremnts.txt

ENTRYPOINT ["python", "main.py"]