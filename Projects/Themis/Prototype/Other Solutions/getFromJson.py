import os         #used to access the folder access and directory change functions
import json       #used for file handling (writing to and reading from)

def getFromJson(directory):     #method to get the judgements data from the JSON file
    os.chdir(directory)         #changes the working directory to the directory taken as a parameter
    
    dictionary = {}             #created empty dictionary
                
    #open JSON file and perform read operations
    with open("D:\\Education\\UoW\\COURSEWORK AND ASSIGNMENTS\\Year 2\\SDGP\\Prototype\\judgements.json", 'r') as file:
        dictionary = json.load(file)            #load the JSON file into the dictionary
        
        count = 0                               #initiate a count variable to keep tracks of keys
        
        for key, value in dictionary.items():   #iterate through the key-value pairs
            print(key)                          #print only the key
            count+=1                            #increment counter
            
        print(count)                            #print the count to see if tally is correct
        
        
getFromJson('D:\\Education\\UoW\\COURSEWORK AND ASSIGNMENTS\\Year 2\\SDGP\\Prototype\\Sample1') #call for function to run