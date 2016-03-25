import time
import os

from PIL import Image
from celery import Celery


app = Celery(
    'taskqueue',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0',
  )

@app.task
def add(a,b):
    time.sleep(5)
    return a + b

@app.task
def sum2(value):
    time.sleep(5)
    return sum(value)

@app.task
def make_thumbnail(path, width, height):
    filepath, ext = os.path.splitext(path)
    output_path = '{}_thum{}'.format(filepath, ext)

    if os.path.exists(output_path):
        return output_path

    im = Image.open(path)
    im.thumbnail((width, height, ), Image.ANTIALIAS)
    im.save(output_path)
    im.close()

    return output_path