import os
import json
import time
import re
from nltk.corpus import stopwords

def cosineSimilarity(directory):
    start_time = time.time()
    os.chdir(directory)
    
    keywords = ['vehicle', 'driver', 'liability', 'employer', 'permit', 'development', 'housing', 'condominium', 'chettiar', 'shares', 'gazette', 'market', 'company', 'property', 'credit', 'seller', 'commercial', 'beneficiary', 'deceased', 'transfer', 'expulsion', 'parliament', 'muslim', 'secretary', 'prescription', 'vendor', 'perches', 'transaction', 'police', 'traffic', 'torture', 'arrested', 'college', 'schools', 'school', 'ministry', 'director', 'foreign', 'employment', 'covenant', 'bureau', 'criminal', 'election', 'livestock', 'bankers', 'corrupt', 'research', 'governors', 'government', 'president', 'agency', 'medical', 'university', 'medicine', 'education', 'ceylinco', 'insurance', 'minister', 'cement', 'import', 'customs', 'trustee', 'students', 'finance', 'library', 'arbitrator', 'salary', 'contract', 'account', 'teacher',  'tenant', 'hiring', 'service', 'divorce', 'murder', 'football', 'union', 'infringement', 'fiscal', 'corpus', 'vehicles', 'indemnity', 'licensee', 'trial', 'adultery', 'labour', 'retire', 'institute', 'trespasser', 'servant', 'lessee', 'estate', 'agriculture', 'probation', 'services', 'landlord', 'swords', 'building', 'municipal', 'coowners', 'payment', 'husband', 'international', 'immunity', 'diplomatic', 'brother', 'security', 'trading', 'mother', 'child', 'children', 'license', 'death', 'injury', 'homicide', 'prosecution', 'assailants', 'solicitor', 'cabinet', 'victim', 'witness', 'timber', 'damages', 'plantation', 'employee', 'bribery', 'interest', 'mortgage', 'pension', 'clinic', 'employees', 'imprisonment', 'liquor', 'forest', 'leasing', 'ceylon', 'boutique', 'factory', 'jewellery', 'obstruction', 'tenement', 'marriage', 'auction', 'house', 'scheme', 'provincial']
    keywordsInQuery = []
    fileList = []
    newWordList = []
    
    with open("D:\\Education\\UoW\\COURSEWORK AND ASSIGNMENTS\\Year 2\\SDGP\\Prototype\\Query.txt", "r",encoding='utf-8') as query:
        for line in query.readlines():
            wordList = line.lower().split()
            newWordList.extend(wordList)
            
            for word in newWordList:
                if word in keywords:
                    keywordsInQuery.append(word)
                    
        print(keywordsInQuery)        
    
    for filename in os.listdir(directory):
         if filename.endswith(".txt"):
             txtFileObj = open (filename, 'r', encoding = "utf-8")
             
             for keyword in keywordsInQuery:
                 stringPresent = re.findall(r' ' + keyword + ' ', txtFileObj.read())
                 
                 if stringPresent:
                     fileList.append(filename)
                     
    print(len(fileList))
    print(fileList)
             
    end_time = time.time()
    print(end_time-start_time)

cosineSimilarity('D:\\Education\\UoW\\COURSEWORK AND ASSIGNMENTS\\Year 2\\SDGP\\Prototype\\TXT (untagged - all)')