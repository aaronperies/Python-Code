import os                         #used to access the folder access and directory change functions
import json as js                 #used to perform operations on JSON file

class Probability:                #declare class for probability (required for back-end)
    
    def calculateProbability():   #function that returns the percentages
        
        directory = ('D:\\Education\\UoW\\COURSEWORK AND ASSIGNMENTS\\Year 2\\SDGP\\Prototype\\Final TXT')
        #this directory variable is used to set the directory of the folder where we will iterate through the PDF documents
        
        os.chdir(directory) #switches working directory
        
        positiveTags = ['<affirmed>']   #list contains the positive tags that will be used in verdicts
        negativeTags = ['<reversed>']   #list contains the negative tags that will be used in verdicts
        neutralTags = ['<other>']       #list contains the neutral tags that will be used in verdicts
        
        fileList = []       #all filenames obtained from the JSON file will be appended to this list
        
        with open("D:\\Education\\UoW\\COURSEWORK AND ASSIGNMENTS\\Year 2\\SDGP\\Prototype\\similarFiles.json", 'r') as file:
            fileList = js.load(file)    #reads JSON file containing list of relevant cases
        
        newWordList = []    #words from the text file will be thrown into this list for further analysing
        
        positive = 0        #keeps track of the number of postive cases from the filenames obtained from fileList
        negative = 0        #keeps track of the number of negative cases from the filenames obtained from fileList
        neutral = 0         #keeps track of the number of neutral cases from the filenames obtained from fileList
        count = 0           #keeps track of the number of total cases from the filenames obtained from fileList
        
        for file in fileList:                       #iterates through all the files in the list read from JSON file
            if file in os.listdir(directory):       #performs operations only if the files are in the directory
                txtFileObj = open (file, 'r', encoding = "utf-8")   #assigns each text file as an object
                count += 1                          #increments the count used to calculate the probability
                
                for line in txtFileObj.readlines(): #iterates through each line in the file
                    wordList = line.lower().split() #creates a list with all the lines converted to lowercase and split into words
                    newWordList.extend(wordList)    #adds each line to new word list in the form of words
                    
                for tag in positiveTags:           #for each tag in the positiveTag List
                    if tag in newWordList:         #if the <affirmed> tag is in the list
                        positive += 1               #increment positive judgement count by 1
                        
                for tag in negativeTags:           #for each tag in the negativeTag List
                    if tag in newWordList:         #if the <reversed> tag is in the list
                        negative += 1               #increment negative judgement count by 1
                 
                for tag in neutralTags:            #for each tag in the neutralTag List
                    if tag in newWordList:         #if the <other> tag is in the list
                        neutral += 1                #increment neutral judgement count by 1
                        
                newWordList.clear()                 #clear the list before the next file is opened
        
        appellantWinProbability = positive/count * 100 #variable that stores the appellants winning percentage
        defendentWinProbability = negative/count * 100 #variable that stores the defendents winning percentage
        neutralProbability = neutral/count * 100       #variable that stores the probability of the case being neutral
        
        #this dictionary stores the percentages to be written to a JSON file
        percentages = {"Positive": appellantWinProbability, "Negative": defendentWinProbability, "Neutral": neutralProbability}
        
        #checking if the json file exists before creating it
        if os.path.exists("D:\\Education\\UoW\\COURSEWORK AND ASSIGNMENTS\\Year 2\\SDGP\\Prototype\\percentages.json"):
            os.remove("D:\\Education\\UoW\\COURSEWORK AND ASSIGNMENTS\\Year 2\\SDGP\\Prototype\\percentages.json")
        
        #creating the JSON file and writing the percentages dictionary to it to be used in the generateVerdicts file
        with open("D:\\Education\\UoW\\COURSEWORK AND ASSIGNMENTS\\Year 2\\SDGP\\Prototype\\percentages.json", 'a') as percentageFile:
            js.dump(percentages, percentageFile)
        
        result=[
               {
                
                'Appellant Win Probability ':appellantWinProbability,
                'Defendent Win Probability ':defendentWinProbability,
                'Neutral Probability ':neutralProbability
                }
              ]
        return (result)
        
        #return appellantWinProbability, defendentWinProbability, neutralProbability  #returns the percentages to be plotted in pie-chart
    
    #calculateProbability()      #runs the probability calculation