from celery.task import task
from apps.website.connector import task_celery


@task
def fav_doctor():
    task_celery()
