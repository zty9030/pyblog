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

import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
render_template, flash

import re



RESULT=['aaaaaa','bbbbbbbbb','ccccccccc']


app = Flask(__name__)

@app.route('/')
def Welcome():
	return render_template('index.html',results=RESULT)

@app.route('/search',methods=['POST'])
def search():
	global RESULT
	term = request.form['term']
	if term=='':
		RESULT=[]
	else:
		RESULT = searchterm(term)
	return redirect(url_for('Welcome'))

@app.route('/line')
def line():
	return app.send_static_file('linechart.html')

port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port))
