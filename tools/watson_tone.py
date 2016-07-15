import json
from watson_developer_cloud import ToneAnalyzerV3

def tone(te):
	tone_analyzer = ToneAnalyzerV3(
   		password =  "FwdYI5O0TaGY",
   		username =  "be8de89c-f720-43eb-beec-9f52093bdb6a",
   		version ='2016-05-19')
	toneresult = json.dumps(tone_analyzer.tone(text=te)['document_tone'])
	return toneresult

