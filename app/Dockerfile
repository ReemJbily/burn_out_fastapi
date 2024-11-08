FROM python:3.12


WORKDIR /code


COPY ./requirments.txt /code/requirments.txt



RUN pip install --no-cache-dir --upgrade -r /code/requirments.txt


COPY ./app.py /code/
COPY ./burn-out-model-catboost.pk1 /code/
EXPOSE 8080

CMD ["fastapi", "deploy:app", "./app.py", "--port", "8080"]