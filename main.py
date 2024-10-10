from feeds import process_and_store_articles
from tasks import process_article
from celery import group

# Fetch and process the articles
def run_etl_pipeline():
    articles = process_and_store_articles()
    task_group = group(process_article.s(article) for article in articles)
    task_group.apply_async()

if __name__ == "__main__":
    run_etl_pipeline()
