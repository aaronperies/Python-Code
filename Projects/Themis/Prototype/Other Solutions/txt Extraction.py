#import nltk
#from urllib import request
#url = "D:\TXT\case1.txt"
#response = request.urlopen(url)
#raw = response.read().decode('utf8')
#type(raw)

#f = open('40_10_sc_appeal.txt', encoding = 'utf-8')
#raw = f.read()

import pandas

dataset = pandas.read_csv('40_10_sc_appeal.txt', delimiter = '\t')
dataset.head()

dataset['word_count'] = dataset['abstract1'].apply(lambda x: len(str(x).split(" ")))
dataset[['the','word_count']].head()

dataset.word_count.describe()

