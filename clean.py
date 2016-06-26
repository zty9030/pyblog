# -*- coding: utf-8 -*-
from TwitterAPI import TwitterAPI
import pandas as pd
import re
from collections import Counter
from nltk.util import ngrams
import matplotlib.pyplot as plt
from wordcloud import WordCloud
def searchterm(term):
	api_key = "GFtGARDLBK1DLx5xUJc24HBDA"
	api_secret = "6SA5i1cigGtSLL4e1FiNJ6MQJgun6YMFB4CHG7U54Lkrhs8bpk"
	access_token_key = "1111734522-aKmSaa9ZLyRmX6gRpxoxBA9uhP0Olkeao3EDKNP"
	access_token_secret = "xEQ0PIATwNdgsuoZoiPovMFjYbWNsCqNcpCZtK5cvyR2Y"

	api = TwitterAPI(api_key, api_secret, access_token_key, access_token_secret)

	search = {'q':term,'lang':'en','count':100}
	j = 0;
	result = []
	while j<200:
		r = api.request('search/tweets', search)
		for item in r:
			search['max_id']= item['id']
			result.append(item['text'])
			j+=1
			if (j%100==0): print j
	return result

def clean_tweets(s):
    stopwords = [u'a',u'about',u'above',u'after',u'again',u'against',u'all',u'am',u'an',u'and',u'any',u'are',u'as',u'at',u'be',
             u'because', u'been', u'before', u'being', u'below', u'between', u'both', u'but', u'by', u'can', u'did',
             u'do', u'does', u'doing',u'don', u'down', u'during', u'each', u'few', u'for', u'from', u'further', u'had', u'has',
             u'have', u'having', u'he', u'her', u'here', u'hers', u'herself', u'him', u'himself', u'his', u'how', u'i', u'if',
             u'in', u'into', u'is', u'it', u'its', u'itself', u'just', u'me', u'more', u'most', u'my', u'myself', u'no', u'nor',
             u'not', u'now', u'of', u'off', u'on', u'once', u'only', u'or', u'other', u'our', u'ours', u'ourselves', u'out',
             u'over', u'own', u's', u'same', u'she', u'should', u'so', u'some', u'such', u't', u'than', u'that', u'the', u'their',
             u'theirs', u'them', u'themselves', u'then', u'there', u'these', u'they', u'this', u'those', u'through', u'to', 
             u'too', u'under', u'until', u'up', u'very', u'was', u'we', u'were', u'what', u'when', u'where', u'which', u'while',
             u'who', u'whom', u'why', u'will', u'with', u'you', u'your', u'yours', u'yourself', u'yourselves']
    #s = re.sub('@.+( |:)',' ', s)
    s = re.sub('\n',' ', s)
    s = re.sub('@', 'ATT', s)
    s = re.sub('http.+( |$)',' ', s)
    s = re.sub('[^A-Za-z]', ' ', s)  
    s = s.replace('RT', ' ')
    s = s.lower().split()
    #s = s.encode('utf-8', errors = 'ignore')
    s = [word for word in s if not word in stopwords]
    s = ' '.join(s)
    return s

#bag of words
def ngram(n):
	ngram = list(ngrams(tweets_string.split(), n))
	ngram = Counter(ngram)
	ngram = ngram.most_common()
	ngram =  ngram[:20] 
	print 'word rank for %s words:' %(n)
	print ngram
	print
	print

#collect tweets
search_term = input('search term:')
data = searchterm(search_term)
data_unique = list(set(data))
tweets = pd.DataFrame(data,columns=['tweets'])
tweets = tweets.drop_duplicates()
  
print 'Collected %s Tweets' %(len(data))
print '%s Unique Tweets' %(len(set(data)))


tweets['tweets_cleaned'] = tweets['tweets'].apply(lambda s: clean_tweets(s))
tweets_clean = list(tweets['tweets_cleaned'].unique())
tweets_string = ' '.join(tweets_clean)
print '%s Unique Tweets after cleaning' %(len(tweets_clean))

ngram(1)
ngram(2)
ngram(3)

wc = WordCloud(background_color="white", max_words=2000)
wc.generate(tweets_string)
plt.imshow(wc)
plt.show()