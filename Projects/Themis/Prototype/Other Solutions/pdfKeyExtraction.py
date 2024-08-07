import nltk
import PyPDF2 as pdf
import math
import pandas as pd
import textract
import re

filename = r"D:\\Education\\UoW\\COURSEWORK AND ASSIGNMENTS\\Year 2\\SDGP\\Prototype\\sample1.pdf"

pdfFileObj = open (filename,'rb')

#this allows you to read the file

pdfReader= pdf.PdfFileReader(pdfFileObj)

num_pages =  pdfReader.numPages

count = 0
text = ""

while count < num_pages:
        pageObj = pdfReader.getPage(count)
        count += 1
        text += pageObj.extractText()
        
if text != "":
    text = text
    
else:
    text = textract.process("",method='tesseract',language='eng')

tokens = [t for t in text.split()] #we split the text we declared before and obtained

from nltk.corpus import stopwords
sr = stopwords.words('english')
clean_tokens = tokens[:]
for token in tokens:
    if len(token) < 6:
        clean_tokens.remove(token)
        
    #if token in sr:
     #   clean_tokens.remove(token)
    
#text = clean_tokens.encode('ascii','ignore').lower()
print(clean_tokens)

text = ' '.join([str(elem) for elem in clean_tokens])

keywords = re.findall(r'[a-zA-Z]\w+', text)
len(keywords)

df = pd.DataFrame(list(set(keywords)),columns=['keywords'])

def weightage(word,text,number_of_documents=1):
    word_list = re.findall(word,text)
    number_of_times_word_appeared = len(word_list)
    tf = number_of_times_word_appeared/float(len(text))
    idf = math.log((number_of_documents)/float(number_of_times_word_appeared))
    tf_idf = tf*idf
    return number_of_times_word_appeared,tf,idf ,tf_idf

df['number_of_times_word_appeared'] = df['keywords'].apply(lambda x: weightage(x,text)[0])
df['tf'] = df['keywords'].apply(lambda x: weightage(x,text)[1])
df['idf'] = df['keywords'].apply(lambda x: weightage(x,text)[2])
df['tf_idf'] = df['keywords'].apply(lambda x: weightage(x,text)[3])

df = df.sort_values('tf_idf',ascending=True)
df.to_csv('Keywords.csv')
df.head(25)

freq = nltk.FreqDist(clean_tokens)
freq.plot(20, cumulative = False)