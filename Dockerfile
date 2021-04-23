FROM python:3.9-alpine

RUN pip install algoliasearch

ADD main.py /main.py

CMD ["python", "/main.py"]