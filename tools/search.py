# -*- coding: utf-8 -*-

from TwitterAPI import TwitterAPI

def searchterm(term):
	api_key = ""
	api_secret = ""
	access_token_key = ""
	access_token_secret = ""

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
