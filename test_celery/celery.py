from __future__ import absolute_import
from celery import Celery

app = Celery(
    'test_celery',
             broker='amqp://rabbitmq:rabbitmq@localhost:5672/my_vhost',
             backend='rpc://',
             include=['test_celery.tasks']
    )