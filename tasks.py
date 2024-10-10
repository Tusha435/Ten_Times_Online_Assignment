from celery import Celery
from classifier import classify_article
from database import store_article

app = Celery('news_processor', broker='pyamqp://guest@localhost//')


@app.task
def process_article(article):
    # Perform NLP Classification
    category = classify_article(article['content'])
    article['category'] = category

    # Store classified article in DB
    store_article(article)
