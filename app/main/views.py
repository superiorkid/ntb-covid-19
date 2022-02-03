from . import main
from flask import render_template
from ..api.covid_data import total_kasus, get_data, kasus_per_kabupaten
from ..covid_content.news_update import get_news

RSS_FEEDS = {
  'indo_gov': 'https://covid19.go.id/feed/berita'
}

@main.route('/')
def index():
  return render_template('index.html', total_kasus=total_kasus(), data=get_data(), kasus_per_kabupaten=kasus_per_kabupaten())

@main.route('/news')
def news():
  news_update = get_news(RSS_FEEDS['indo_gov'])
  articles = [i for i in news_update.get('posts')[:6]]

  return render_template('news.html', articles=articles, news_update=news_update)

@main.route('/about')
def about():
  urls = {
    'github': 'https://github.com/superiorkid',
    'api': 'https://corona.ntbprov.go.id/api/data',
    'rss_feed': 'https://covid19.go.id/feed/berita'
  }

  return render_template('about.html', urls=urls)