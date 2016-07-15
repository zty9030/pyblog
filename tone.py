import json
from watson_developer_cloud import ToneAnalyzerV3

tone_analyzer = ToneAnalyzerV3(
   password =  "FwdYI5O0TaGY",
   username =  "be8de89c-f720-43eb-beec-9f52093bdb6a",
   version ='2016-05-19')

t = open('test.txt','r').read()

print(json.dumps(tone_analyzer.tone(text=t),indent=2))