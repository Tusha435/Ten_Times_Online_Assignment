import feedparser
from datetime import datetime
from database import store_article

# List of RSS feed URLs
rss_feeds = [
    'http://rss.cnn.com/rss/cnn_topstories.rss',
    'http://qz.com/feed',
    'http://feeds.foxnews.com/foxnews/politics',
    'http://feeds.reuters.com/reuters/businessNews',
    'http://feeds.feedburner.com/NewshourWorld',
    'https://feeds.bbci.co.uk/news/world/asia/india/rss.xml'
]

def fetch_rss_feeds():
    feeds = [
        'http://rss.cnn.com/rss/cnn_topstories.rss',
        'http://qz.com/feed',
        'http://feeds.foxnews.com/foxnews/politics',
        'http://feeds.reuters.com/reuters/businessNews',
        'http://feeds.feedburner.com/NewshourWorld',
        'https://feeds.bbci.co.uk/news/world/asia/india/rss.xml'
    ]

    articles = []
    for feed in feeds:
        parsed_feed = feedparser.parse(feed)
        for entry in parsed_feed.entries:
            article = {
                'title': entry.title,
                'url': entry.link,
                'published_at': entry.published if 'published' in entry else None,
                'content': entry.summary if 'summary' in entry else entry.description if 'description' in entry else '',  # Check for summary or description
                'source': feed
            }
            articles.append(article)
    return articles


def run_etl_pipeline():
    articles = process_and_store_articles()
    if articles is None or not articles:
        raise ValueError("No articles processed.")

    # Use the articles in your task group
    task_group = group(process_article.s(article) for article in articles)
    # Proceed with the rest of your logic


def fetch_articles():
    # This function should return a list of article data
    return [
        {"title": "Article 1", "url": "https://example.com/article1"},
        {"title": "Article 2", "url": "https://example.com/article2"},
    ]


def store_article(article_data):
    # Your logic to store the article in the database
    pass  # Replace this with actual database storing logic


def process_and_store_articles():
    fetched_article_data = fetch_articles()
    print("Fetched Articles:", fetched_article_data)  # Debugging statement

    if not fetched_article_data:
        raise ValueError("No articles fetched.")

    articles = []
    for article_data in fetched_article_data:
        store_article(article_data)
        articles.append(article_data)

    return articles
