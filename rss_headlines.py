# This python code will take a list of RSS newsfeed urls, fetch and combine all the news headlines into one list.
# The feedparser package is required, install it with the following command.


import feedparser


# Function to fetch the rss feed and return the parsed RSS
def parse_rss(rss_url):
    return feedparser.parse(rss_url)


# Function grabs the rss feed headlines (titles) and returns them as a list
def get_headlines(rss_url):
    headlines = []

    feed = parse_rss(rss_url)
    for newsitem in feed['items']:
        headlines.append(newsitem['title'])

    return headlines


# Driver code to aggregate newsfeed headlines from different sources
# We will list a bunch of news sources to select from to receive the feeds from.
# The user can see all the items in a beautiful cli
def main():
    # A list to hold all headlines
    allheadlines = []

    # List of RSS feeds that we will fetch and combine
    newsurls = {
        'toi': 'http://timesofindia.indiatimes.com/rssfeedstopstories.cms?x=1',
        'googlenews': 'https://news.google.com/news/rss/?hl=en&amp;ned=us&amp;gl=US',
        'yahoonews': 'http://news.yahoo.com/rss/',
        'firstpost': 'http://www.firstpost.com/feed/rss',
    }

    # Iterate over the feed urls
    for key, url in newsurls.items():
        # Call getHeadlines() and combine the returned headlines with allheadlines
        allheadlines.extend(get_headlines(url))

    # Iterate over the allheadlines list and print each headline
    for hl in allheadlines:
        print(hl)

    # end of code

main()