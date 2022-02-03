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
        temp['author'] = post.author
        temp['time_published'] = post.published
        temp['tags'] = [tag.term for tag in post.tags]
        temp['authors'] = [author.name for author in post.authors]
        temp['summary'] = post.summary
        temp['media_thumbnail'] = post.media_content[0]['url']
      except:
        pass

      post_list.append(temp)

    posts_details['posts'] = post_list
    
    return posts_details

  else:

    return None