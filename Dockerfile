FROM tiangolo/uwsgi-nginx-flask:python3.8

COPY /app/app/requirements.txt /tmp/

RUN pip install -r /tmp/requirements.txt

COPY ./app /app

CMD ["python","main.py"]

