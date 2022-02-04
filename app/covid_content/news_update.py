import feedparser

def get_news(publication):
  if publication is not None:
    blog_feed = feedparser.parse(publication)
    posts = blog_feed.entries

    posts_details = {
      "blog_title": blog_feed.feed.title,
      "blog_link": blog_feed.feed.link
    }

    post_list = list()

    for post in posts:
      temp = dict()

      try:
        temp['title'] = post.title
        temp['link'] = post.link
        temp['time_published'] = post.published
        temp['media_thumbnail'] = post.enclosures[0]['url']
        # temp['summary'] = post.summary 
      except:
        pass

      post_list.append(temp)

    posts_details['posts'] = post_list
    
    return posts_details