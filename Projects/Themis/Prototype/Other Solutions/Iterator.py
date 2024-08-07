import os                 #used to access files and folders easily
import PyPDF2 as pdf      #used to operate on PDF documents in python
import nltk
import pandas as pd
import textract
import re
import math
 
directory = ('D:\\Education\\UoW\\COURSEWORK AND ASSIGNMENTS\\Year 2\\SDGP\\Prototype\\PDF')
#this directory variable is used to set the directory of the folder where we will iterate through the PDF documents

print(os.getcwd())  #prints current working directory
os.chdir(directory) #switches working directory

def weightage(word,text,number_of_documents=1):
    word_list = re.findall(word,text)
    number_of_times_word_appeared = len(word_list)
    tf = number_of_times_word_appeared/float(len(text))
    idf = math.log((number_of_documents)/float(number_of_times_word_appeared))
    tf_idf = tf*idf
    return number_of_times_word_appeared,tf,idf ,tf_idf

for filename in os.listdir(directory):
    if filename.endswith(".pdf"):
        pdfFileObj = open (filename, 'rb')

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
            
            if len(token) < 5:
                clean_tokens.remove(token)
                
            #if token in sr:
             #   clean_tokens.remove(token)
                
        #text = clean_tokens.encode('ascii','ignore').lower()
        print(clean_tokens)
        
        lawTerms = ['Plaintiff', 'plaintiff', 'appellate', 'appellant', 'Respondent', 
                    'Petitioner', 'Appeal', 'appeal', 'petition', 'respondent']
        
# =============================================================================
#         for word in clean_tokens:
#             for phrase in lawTerms:
#                 if word == phrase:
#                     clean_tokens.remove(word)
# =============================================================================
        
        text = ' '.join([str(elem) for elem in clean_tokens])

        keywords = re.findall(r'[a-zA-Z]\w+', text)
        print(len(keywords))
        
        df = pd.DataFrame(list(set(keywords)),columns=['keywords'])

        df['number_of_times_word_appeared'] = df['keywords'].apply(lambda x: weightage(x,text)[0])
        df['tf'] = df['keywords'].apply(lambda x: weightage(x,text)[1])
        df['idf'] = df['keywords'].apply(lambda x: weightage(x,text)[2])
        df['tf_idf'] = df['keywords'].apply(lambda x: weightage(x,text)[3])
        
        df = df.sort_values('tf_idf',ascending=True)
        #df.to_csv('Keywords.csv')
        df.head(25)

        freq = nltk.FreqDist(clean_tokens)
        freq.plot(5, cumulative = False)           
        
        #for word in keywords:
        #    if keywords.count(word) < 30:
        #        keywords.remove(word)
                
        #print(len(keywords))
        #print(keywords)