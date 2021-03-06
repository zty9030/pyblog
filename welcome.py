# -*- coding: utf-8 -*-


# Copyright 2015 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from tools.search import searchterm
from tools.clean import clean_tweets,drop_duplicate
from tools.analysis import bagofword
from tools.watson_tone import tone

import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
render_template, flash

import re
import json


RESULT={'tweet':['a','bb','ccc','a bb ee ccc'],'term':''}
ANALYSIS = {}

app = Flask(__name__)

@app.route('/')
def Welcome():
	return render_template('index.html',results=RESULT)

@app.route('/search',methods=['POST'])
def search():
	global RESULT
	RESULT['term'] = request.form['term']
	if RESULT['term']=='':
		RESULT['tweet']=[]
	else:
		RESULT['tweet']= [clean_tweets(i) for i in searchterm(RESULT['term'])]
		RESULT['tweet_original'] = drop_duplicate(searchterm(RESULT['term']))
		RESULT['onum'] = len(RESULT['tweet'])
		RESULT['tweet'] = drop_duplicate(RESULT['tweet'])
		RESULT['fnum'] = len(RESULT['tweet'])
	return redirect(url_for('Welcome'))

@app.route('/analysis')
def  analysis():
	global ANALYSIS
	ANALYSIS['bag'] = bagofword(RESULT['tweet'],1)
	ANALYSIS['bag'] = json.dumps(ANALYSIS['bag'])
	ANALYSIS['tone'] = tone('\n'.join(RESULT['tweet']))
	return render_template("analysis.html",analysis=ANALYSIS)

port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0',port=int(port))
