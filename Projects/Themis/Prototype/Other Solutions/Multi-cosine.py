import os
import time
import threading

from nltk.corpus import stopwords


def cosineSimilarity(directory):
    start_time = time.time()
    #directory = ('C:\\Users\\user\\Desktop\\Level 5\\Software Development Group Project\\Sample txt')
    os.chdir(directory)
    
    newWordList=[]
    
    count=0
    clean_tokens=[]
    clean_tokens2=[]
    
    for filename in os.listdir(directory):
         if filename.endswith(".txt"):
    
            txtFileObj = open (filename, 'r', encoding = "utf-8")
            count += 1
            
            newWordList.clear()
            for line in txtFileObj.readlines():
                wordList = line.lower().split()
                newWordList.extend(wordList)
                     
                sr = stopwords.words('english')
                clean_tokens.clear()
                clean_tokens = newWordList[:]
                              
                for token in newWordList:
                    if len(token) < 5:
                        clean_tokens.remove(token)
                
    # =============================================================================
    #         gen_docs = [[w.lower() for w in word_tokenize(text)]
    #         for text in clean_tokens]
    # 
    #         dictionary = gensim.corpora.Dictionary(gen_docs)
    #         print(dictionary.token2id)
    #         corpus = [dictionary.doc2bow(gen_docs) for gen_docs in gen_docs]
    # =============================================================================
    
    #==============================Query Document==========================================
    
            newWordList2=[]
            with open("D:\\Education\\UoW\\COURSEWORK AND ASSIGNMENTS\\Year 2\\SDGP\\Prototype\\TXT (untagged - all)\\sc_appeal_15_2010.txt", "r", encoding="utf-8") as f:
                for line in f.readlines():
                    wordList = line.lower().split()
                    newWordList2.extend(wordList)
                     
            sr = stopwords.words('english')
            clean_tokens2.clear()
            clean_tokens2 = newWordList2[:]
                    
            for token in newWordList2:
                if len(token) < 5:
                    clean_tokens2.remove(token)
             
            setList1=[]
            setList2=[]
            
            vector= set(clean_tokens).union(set(clean_tokens2))
            for i in vector:
                    if i in clean_tokens:
                        setList1.append(1)
                    else:
                        setList1.append(0)
                     
                    if i in clean_tokens2:
                        setList2.append(1)
                    else:
                        setList2.append(0)
                 
            c=0
                 
            for y in range(len(vector)):
                    c+=setList1[y]*setList2[y]
             
            cosine = c/float((sum(setList1)*sum(setList2))**0.5)
            print ("Similarity: ",cosine*100,"%", filename)
            end_time = time.time()
            print(end_time-start_time)
             
p1 = threading.Thread(target=cosineSimilarity('D:\\Education\\UoW\\COURSEWORK AND ASSIGNMENTS\\Year 2\\SDGP\\Prototype\\Sample1'), args=(10, )) 
p2 = threading.Thread(target=cosineSimilarity('D:\\Education\\UoW\\COURSEWORK AND ASSIGNMENTS\\Year 2\\SDGP\\Prototype\\Sample2'), args=(10, ))
p3 = threading.Thread(target=cosineSimilarity('D:\\Education\\UoW\\COURSEWORK AND ASSIGNMENTS\\Year 2\\SDGP\\Prototype\\Sample3'), args=(10, ))
p4 = threading.Thread(target=cosineSimilarity('D:\\Education\\UoW\\COURSEWORK AND ASSIGNMENTS\\Year 2\\SDGP\\Prototype\\Sample4'), args=(10, ))
#p1 = multiprocessing.Process(target=cosineSimilarity('C:\\Users\\user\\Desktop\\Level 5\\Software Development Group Project\\Sample txt'), args=(10, ))
#p2 = multiprocessing.Process(target=cosineSimilarity('C:\\Users\\user\\Desktop\\Level 5\\Software Development Group Project\\Outsourced Text Files\\Krissy txt'), args=(10, )) 
# p3 = multiprocessing.Process(target=cosineSimilarity(), args=(10, )) 
# p4 = multiprocessing.Process(target=cosineSimilarity(), args=(10, ))
# =============================================================================
        
p1.start()
p2.start()
p3.start()
p4.start()
# =============================================================================

p1.join()        
p2.join()   
p3.join()
p4.join()
# =============================================================================
        
print("Done")