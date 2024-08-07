import os                               #used to access the folder access and directory change functions
import json                             #used for file handling (writing to and reading from)
import time                             #used to measure the time taken for the program to run (experimental purposes)
import re                               #used to clean punctuation
import nltk

def extractKeywords(directory):      #method to write the judgements data to the JSON file
    os.chdir(directory)          #changes the working directory to the directory taken as a parameter
    newWordList=[]               #list to contain the words extracted from each judgement
    
    clean_tokens=[]              #contains all the words in the text besides the stopwords
    dictionary = {}              #used to store the filename and the judgement
    
    for filename in os.listdir(directory):      #iterates through all the files in the directory specified in parameters
         if filename.endswith(".txt"):          #performs operations only if the files are in .txt format

                  txtFileObj = open (filename, 'r', encoding = "utf-8")     #assigns each text file as an object
                  newWordList.clear()           #clears newWordList with each iteration
                  
                  for line in txtFileObj.readlines():           #iterates through each line in the file
                      wordList = line.lower().split()           #creates a list with all the lines converted to lowercase and split into words
                      newWordList.extend(wordList)              #adds each line to new word list in the form of words
                           
                      clean_tokens = newWordList[:]             #assigns the clean_tokens list with all the words in newWordList
                                    
                      for token in newWordList:                 #iterates through each word in the list
                           if len(token) <= 5:                   #checks if the length of the word is less than or equal to 5 characters
                               clean_tokens.remove(token)        #removes if condition is satisfied
                               
                      clean_tokens=[re.sub(r'[^\w\s]','',x) for x in clean_tokens]  #Cleaning all the punctuation.      
    
                  freq = nltk.FreqDist(clean_tokens)
                  freq.plot(20, cumulative = False)

start_time = time.time()                #starts timer at program execution start
extractKeywords('D:\\Education\\UoW\\COURSEWORK AND ASSIGNMENTS\\Year 2\\SDGP\\Prototype\\Sample1')   #calls for the function to run
end_time = time.time()                  #ends the timer after function has completed running
print(end_time-start_time)              #prints the time taken in seconds to run the program. (came upto 11,006 seconds when run)