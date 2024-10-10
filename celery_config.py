from celery import Celery

# Connect to RabbitMQ (running on localhost)
app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def process_article(article):
    # Task logic here
    print(f"Processing article: {article['title']}")
app = Celery('tasks', broker='redis://localhost:6379/0')
app = Celery('tasks', broker='redis://your-server-ip:6380/0')

