FROM  207457565/school:latest

COPY . /project

WORKDIR /project

#RUN  pip install -r requiremnts.txt

ENTRYPOINT ["python", "main.py"]