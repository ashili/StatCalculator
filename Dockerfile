FROM python:3.8

ADD . .

RUN pip install --upgrade pip

CMD ["python", "-m", "unittest","discover", "-s", "Tests"]
