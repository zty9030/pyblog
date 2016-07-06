import re
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
    s = [word for word in s if len(word) > 2]
    s = ' '.join(s)
    return s

def drop_duplicate(li):
    return list(set(li))