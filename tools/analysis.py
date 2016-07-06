from collections import Counter
from nltk.util import ngrams
def bagofword(li,n):
	tweets_string = ' '.join(li)
	ngram = [ ' '.join(i[:n]) for i in ngrams(tweets_string.split(), n)]	
	ngram = Counter(ngram)
	ngram = ngram.most_common()
	ngram = ngram[:20]
	ligram =[]
	for i in ngram:
		di = dict()
		di['text'] = i[0]
		di['weight']=i[1]
		ligram.append(di)
	return ligram
