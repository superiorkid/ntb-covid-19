from . import main
from flask import render_template
from ..api.covid_data import total_kasus, get_data, kasus_per_kabupaten
from ..covid_content.news_update import get_news
import feedparser

RSS_FEEDS = {
  'republika': 'http://www.republika.co.id/rss'
}

@main.route('/')
def index():
  return render_template('index.html', total_kasus=total_kasus(), data=get_data(), kasus_per_kabupaten=kasus_per_kabupaten())

@main.route('/news')
def news():
  news_update = get_news(RSS_FEEDS['republika'])
  articles = [i for i in news_update.get('posts')]

  return render_template('news.html', articles=articles, news_update=news_update)

  