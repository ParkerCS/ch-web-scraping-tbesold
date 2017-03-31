# Go to your favorite follow on Twitter.  (not someone who posts explicit materials please)
# Inspect their twitter feed.
# You'll notice that the tweets are stored in a ordered list <ol></ol>,
# and individual tweets are contained as list items <li></li>.
# Use BeautifulSoup and urllib to grab the text contents of the tweets
# located on the twitter page you chose.  The .text attribute will supply the content of a soup object.
# Have fun.  Again, nothing explicit. (15pts)

from bs4 import BeautifulSoup
import urllib.request


url = "https://twitter.com/williegdi?lang=en"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read(), "html.parser")

tweets = [x.text.strip() for x in soup.findAll('p', {'class' :"TweetTextSize TweetTextSize--large js-tweet-text tweet-text"})]
for i in range(len(tweets)):
    print(tweets[i])

