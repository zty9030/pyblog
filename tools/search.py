# -*- coding: utf-8 -*-

from TwitterAPI import TwitterAPI

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