FROM python:3.7


WORKDIR /app
COPY . .
RUN pip install -r test_celery/requirements.txt

CMD ["celery", "-A test_celery worker --loglevel=info"]