import json
from watson_developer_cloud import ToneAnalyzerV3Beta

tone_analyzer = ToneAnalyzerV3Beta(
   username='ef1151ed-416c-4839-9d46-410d0fcd1c58',
   password='x2UemSriWcam',
   version='2016-05-19')

t = open('test.txt','r').read()

print(json.dumps(tone_analyzer.tone(text=t),indent=2))