from celery import Celery
from .celery import app

@app.task
def add(x, y):
    return x + y
