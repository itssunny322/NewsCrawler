from newsfetch.google import google_search
from newsfetch.news import newspaper
from .models import *

def my_scheduled_job():
    list = ['sports', 'politics', 'weather', 'india', 'tech', 'entertainment', 'bollywood', 'television', 'movie',
            'Fashion',
            'blogs', 'pandemic', 'corona', 'lockdown', 'business', 'economy']

    for each in list:
        a = google_search(each, 'https://timesofindia.indiatimes.com/')
        print("hi")
        print(a.urls)

        for each in a.urls:
            news = newspaper(each)
            new = News()
            new.headline = news.headline
            new.url = each
            new.date = news.date_publish
            # new.author = news.author
            new.article = news.article
            new.source = news.source_domain
            new.save()