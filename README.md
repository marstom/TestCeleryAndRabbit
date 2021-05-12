# How to use

Rabbit dashboard:
http://localhost:15672/#/

docker-compose build
docker-compose up

Now run some long task!

```bash
docker container exec -it my_worker bash
```

In container bash run:

```bash

python -m test_celery.run_tasks &
python -m test_celery.run_tasks &
python -m test_celery.run_tasks &
```

and look at results and dashboard.
