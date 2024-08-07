import os                #used to access the folder access and directory change functions
import json as js        #used to perform operations on JSON file
import numpy as np       #used to perform vectorization
import pickle            #storage medium such as json
import tqdm              #used for progress presentation
from keras.models import Sequential   #to rebuild the model
from keras.layers import Dense, LSTM  #same layers have to be used as when training

keywords = ['murder', 'child', 'land', 'contract', 'employee', 'commercial', 'government']
  
with open("D:\\Education\\UoW\\COURSEWORK AND ASSIGNMENTS\\Year 2\\SDGP\\Prototype\\queryKeywords.json", 'r') as queryKeywords:
    keywordsInQuery = js.load(queryKeywords)
    
#reading the JSON file containing the percentages written to from the probability calculation
with open("D:\\Education\\UoW\\COURSEWORK AND ASSIGNMENTS\\Year 2\\SDGP\\Prototype\\percentages.json", 'r') as percenatgeFile:
    percentages = js.load(percenatgeFile) 
    #assigns a new dictionary named percentages with the values of the dictionary in JSON
    
positiveProbability = 35#percentages.get("Positive")      #obtain the positive probability
negativeProbability = 55#percentages.get("Negative")      #obtain the negative probability
neutralProbability = 10#percentages.get("Neutral")        #obtain the neutral probability
    
class GenerateVerdicts:     #class containing the generating methods
    
    def generateMurderVerdicts():        #define method name (there will be multiple methods here, to generate a variety of verdicts)
        
        # we will be checking which percentage is higher and generate a verdict for that type (positive, negative or neutral)
        if (positiveProbability > negativeProbability) and (positiveProbability > neutralProbability):
            sample = "considering the decisions"
            startingSequence = sample
            
            os.chdir('D:\\Education\\UoW\\COURSEWORK AND ASSIGNMENTS\\Year 2\\SDGP\\Prototype\\Murder Model Results\\Positive')
            
            #retrieve stored dictionaries
            char2int = pickle.load(open("positiveMurderchar2int.pickle", "rb"))
            int2char = pickle.load(open("positiveMurderint2char.pickle", "rb"))
            
            characterCount = 480           #number of characters to be used in the generatedVerdict verdict
            uniqueCharacterCount = len(char2int)
                
            # here we build the model again but instead of training the model we load its best weight
            # the best weight contains the result where the loss was at a minimum and the accuracy at a peak
            # take note that the model must be built in the exact same way as the trained model
            # the number of layers, nodes and activation types cannot be varying between the 2
            model = Sequential([
                LSTM(128, return_sequences = True, input_shape=(characterCount, uniqueCharacterCount)),
                LSTM(256, return_sequences = True),
                LSTM(512),
                Dense(uniqueCharacterCount, activation="softmax"),
            ])
            
            model.load_weights("results/wonderland-v1-0.02.h5")
            
        elif (negativeProbability > positiveProbability) and (negativeProbability > neutralProbability):
            sample = "in the circumstances"
            startingSequence = sample
            
            os.chdir('D:\\Education\\UoW\\COURSEWORK AND ASSIGNMENTS\\Year 2\\SDGP\\Prototype\\Murder Model Results\\Negative')
            
            char2int = pickle.load(open("murderNegativechar2int.pickle", "rb"))
            int2char = pickle.load(open("murderNegativeint2char.pickle", "rb"))
            
            characterCount = 480          
            uniqueCharacterCount = len(char2int)
            
            model = Sequential([
                LSTM(128, return_sequences = True, input_shape=(characterCount, uniqueCharacterCount)),
                LSTM(256, return_sequences = True),
                LSTM(512),
                Dense(uniqueCharacterCount, activation="softmax"),
            ])
            
            model.load_weights("results/wonderland-v1-0.03.h5")
            
        #this bit comes outside the loop because its the same for all 3 if conditions        
        generatedVerdict = ""
        
        for i in tqdm.tqdm(range(characterCount), "Generating verdict"):       # we will be generating 480 characters
            X = np.zeros((1, characterCount, uniqueCharacterCount))                  # make the input sequence
            
            for t, char in enumerate(sample):
                X[0, (characterCount - len(sample)) + t, char2int[char]] = 1
                
            predictCharacter = model.predict(X, verbose=0)[0]        # predict the next character
            vecToInt = np.argmax(predictCharacter)                   # converting the vector to an integer
            intToChar = int2char[vecToInt]                           # converting the integer to a character
            generatedVerdict += intToChar                            # add the character to results
            sample = sample[1:] + intToChar                          # shift sample and the predictCharacter character
                
        finalVerdict = startingSequence + generatedVerdict          #assigns a new variable to the combined verdict
        
        result = [
                 {
                     
                  'Generated Verdict ':finalVerdict
                  }
                ]
        
        return (result)
        
    def generateChildVerdicts():        #method for generating the child verdicts
        
        if (positiveProbability > negativeProbability) and (positiveProbability > neutralProbability):    
            sample = "i answer all the questions"
            startingSequence = sample
            
            os.chdir('D:\\Education\\UoW\\COURSEWORK AND ASSIGNMENTS\\Year 2\\SDGP\\Prototype\\Child Model Results\\Positive')
            
            char2int = pickle.load(open("childPositivechar2int.pickle", "rb"))
            int2char = pickle.load(open("childPositiveint2char.pickle", "rb"))
            
            characterCount = 240           
            uniqueCharacterCount = len(char2int)
            
            model = Sequential([
                LSTM(128, return_sequences = True, input_shape=(characterCount, uniqueCharacterCount)),
                LSTM(256, return_sequences = True),
                LSTM(512),
                Dense(uniqueCharacterCount, activation="softmax"),
            ])
            
            model.load_weights("positiveResults/verdictland-v1-0.02.h5")
            
        elif (negativeProbability > positiveProbability) and (negativeProbability > neutralProbability):
            sample = "for the aforesaid reasons"
            startingSequence = sample
            
            os.chdir('D:\\Education\\UoW\\COURSEWORK AND ASSIGNMENTS\\Year 2\\SDGP\\Prototype\\Child Model Results\\Negative')
            
            char2int = pickle.load(open("childNegativechar2int.pickle", "rb"))
            int2char = pickle.load(open("childNegativeint2char.pickle", "rb"))
            
            characterCount = 240           
            uniqueCharacterCount = len(char2int)
             
            model = Sequential([
                LSTM(128, return_sequences = True, input_shape=(characterCount, uniqueCharacterCount)),
                LSTM(256, return_sequences = True),
                LSTM(512),
                Dense(uniqueCharacterCount, activation="softmax"),
            ])
            
            model.load_weights("negativeResults/verdictland-v1-0.03.h5")
             
        #this bit comes outside the loop because its the same for all 3 if conditions        
        generatedVerdict = ""
        
        for i in tqdm.tqdm(range(characterCount), "Generating verdict"):       
            X = np.zeros((1, characterCount, uniqueCharacterCount))                  
            
            for t, char in enumerate(sample):
                X[0, (characterCount - len(sample)) + t, char2int[char]] = 1
                
            predictCharacter = model.predict(X, verbose=0)[0]          
            vecToInt = np.argmax(predictCharacter)                   
            intToChar = int2char[vecToInt]                   
            generatedVerdict += intToChar                              
            sample = sample[1:] + intToChar                     
                
        finalVerdict = startingSequence + generatedVerdict
        print(finalVerdict)
    
        result = [
                 {
                     
                  'Generated Verdict ':finalVerdict
                  }
                ]
        
        return (result)    
    
    def generateCommercialVerdicts():   #method for generating the commercial verdicts
        
        if (positiveProbability > negativeProbability) and (positiveProbability > neutralProbability):    
            sample = "for the foregoing reasons"
            startingSequence = sample
            
            os.chdir('D:\\Education\\UoW\\COURSEWORK AND ASSIGNMENTS\\Year 2\\SDGP\\Prototype\\Commercial Model Results\\Positive')
            
            char2int = pickle.load(open("commercialPositivechar2int.pickle", "rb"))
            int2char = pickle.load(open("commercialPositiveint2char.pickle", "rb"))
            
            characterCount = 240           
            uniqueCharacterCount = len(char2int)
            
            model = Sequential([
                LSTM(128, return_sequences = True, input_shape=(characterCount, uniqueCharacterCount)),
                LSTM(256, return_sequences = True),
                LSTM(512),
                Dense(uniqueCharacterCount, activation="softmax"),
            ])
            
            model.load_weights("positiveResults/verdictland-v1-0.03.h5")
            
        elif (negativeProbability > positiveProbability) and (negativeProbability > neutralProbability):
            sample = "for the above reasons i see no"
            startingSequence = sample
            
            os.chdir('D:\\Education\\UoW\\COURSEWORK AND ASSIGNMENTS\\Year 2\\SDGP\\Prototype\\Commercial Model Results\\Negative')
            
            char2int = pickle.load(open("commercialNegativechar2int.pickle", "rb"))
            int2char = pickle.load(open("commercialNegativeint2char.pickle", "rb"))
            
            characterCount = 250          
            uniqueCharacterCount = len(char2int)
            
            model = Sequential([
                LSTM(128, return_sequences = True, input_shape=(characterCount, uniqueCharacterCount)),
                LSTM(256, return_sequences = True),
                LSTM(512),
                Dense(uniqueCharacterCount, activation="softmax"),
            ])
            
            model.load_weights("negativeResults/verdictland-v1-0.01.h5")
            
        generatedVerdict = ""
        
        for i in tqdm.tqdm(range(characterCount), "Generating verdict"):       
            X = np.zeros((1, characterCount, uniqueCharacterCount))                  
            
            for t, char in enumerate(sample):
                X[0, (characterCount - len(sample)) + t, char2int[char]] = 1
                
            predictCharacter = model.predict(X, verbose=0)[0]          
            vecToInt = np.argmax(predictCharacter)                   
            intToChar = int2char[vecToInt]                   
            generatedVerdict += intToChar                              
            sample = sample[1:] + intToChar                     
                
        finalVerdict = startingSequence + generatedVerdict
        print(finalVerdict)
        
        result = [
                 {
                     
                  'Generated Verdict ':finalVerdict
                  }
                ]
        
        return (result)
    
    def generateEmployeeVerdicts():     #method for generating the employee verdicts
        if (positiveProbability > negativeProbability) and (positiveProbability > neutralProbability):    
            sample = "i therefore answer the questions of law raised"
            startingSequence = sample
            
            os.chdir('D:\\Education\\UoW\\COURSEWORK AND ASSIGNMENTS\\Year 2\\SDGP\\Prototype\\Employee Model Results\\Positive')
            
            char2int = pickle.load(open("employeePositivechar2int.pickle", "rb"))
            int2char = pickle.load(open("employeePositiveint2char.pickle", "rb"))
            
            characterCount = 120     #400      
            uniqueCharacterCount = len(char2int)
            
            model = Sequential([
                LSTM(128, return_sequences = True, input_shape=(characterCount, uniqueCharacterCount)),
                LSTM(256, return_sequences = True),
                LSTM(512),
                Dense(uniqueCharacterCount, activation="softmax"),
            ])
            
            model.load_weights("positiveResults/verdictland-v1-0.03.h5")
            
        elif (negativeProbability > positiveProbability) and (negativeProbability > neutralProbability):
            sample = "i dismiss the appeal"
            startingSequence = sample
            
            os.chdir('D:\\Education\\UoW\\COURSEWORK AND ASSIGNMENTS\\Year 2\\SDGP\\Prototype\\Employee Model Results\\Negative')
            
            char2int = pickle.load(open("employeeNegativechar2int.pickle", "rb"))
            int2char = pickle.load(open("employeeNegativeint2char.pickle", "rb"))
            
            characterCount = 250           
            uniqueCharacterCount = len(char2int)
            
            model = Sequential([
                LSTM(128, return_sequences = True, input_shape=(characterCount, uniqueCharacterCount)),
                LSTM(256, return_sequences = True),
                LSTM(512),
                Dense(uniqueCharacterCount, activation="softmax"),
            ])
            
            model.load_weights("negativeResults/verdictland-v1-0.03.h5")
            
        generatedVerdict = ""
        
        for i in tqdm.tqdm(range(characterCount), "Generating verdict"):       
            X = np.zeros((1, characterCount, uniqueCharacterCount))                  
            
            for t, char in enumerate(sample):
                X[0, (characterCount - len(sample)) + t, char2int[char]] = 1
                
            predictCharacter = model.predict(X, verbose=0)[0]          
            vecToInt = np.argmax(predictCharacter)                   
            intToChar = int2char[vecToInt]                   
            generatedVerdict += intToChar                              
            sample = sample[1:] + intToChar                     
                
        finalVerdict = startingSequence + generatedVerdict
        print(finalVerdict)
        
        result = [
                 {
                     
                  'Generated Verdict ':finalVerdict
                  }
                ]
        
        return (result)
            
    def generateContractVerdicts():     #method for generating the contract verdicts
        
        if (positiveProbability > negativeProbability) and (positiveProbability > neutralProbability):    
            sample = "i answer the questions of law"
            startingSequence = sample
            
            os.chdir('D:\\Education\\UoW\\COURSEWORK AND ASSIGNMENTS\\Year 2\\SDGP\\Prototype\\Contract Model Results\\Positive')
            
            char2int = pickle.load(open("contractPositivechar2int.pickle", "rb"))
            int2char = pickle.load(open("contractPositiveint2char.pickle", "rb"))
            
            characterCount = 190           
            uniqueCharacterCount = len(char2int)
            
            model = Sequential([
                LSTM(128, return_sequences = True, input_shape=(characterCount, uniqueCharacterCount)),
                LSTM(256, return_sequences = True),
                LSTM(512),
                Dense(uniqueCharacterCount, activation="softmax"),
            ])
            
            model.load_weights("positiveResults/verdictland-v1-0.02.h5")
            
        elif (negativeProbability > positiveProbability) and (negativeProbability > neutralProbability):
            sample = "therefore i answer all the"
            startingSequence = sample
            
            os.chdir('D:\\Education\\UoW\\COURSEWORK AND ASSIGNMENTS\\Year 2\\SDGP\\Prototype\\Contract Model Results\\Negative')
            
            char2int = pickle.load(open("contractNegativechar2int.pickle", "rb"))
            int2char = pickle.load(open("contractNegativeint2char.pickle", "rb"))
            
            characterCount = 250           
            uniqueCharacterCount = len(char2int)
            
            model = Sequential([
                LSTM(128, return_sequences = True, input_shape=(characterCount, uniqueCharacterCount)),
                LSTM(256, return_sequences = True),
                LSTM(512),
                Dense(uniqueCharacterCount, activation="softmax"),
            ])
            
            model.load_weights("negativeResults/verdictland-v1-0.02.h5")
            
        generatedVerdict = ""
        
        for i in tqdm.tqdm(range(characterCount), "Generating verdict"):       
            X = np.zeros((1, characterCount, uniqueCharacterCount))                  
            
            for t, char in enumerate(sample):
                X[0, (characterCount - len(sample)) + t, char2int[char]] = 1
                
            predictCharacter = model.predict(X, verbose=0)[0]          
            vecToInt = np.argmax(predictCharacter)                   
            intToChar = int2char[vecToInt]                   
            generatedVerdict += intToChar                              
            sample = sample[1:] + intToChar                     
            
        finalVerdict = startingSequence + generatedVerdict
        print(finalVerdict)
        
        result = [
                 {
                     
                  'Generated Verdict ':finalVerdict
                  }
                ]
        
        return (result)
            
    def generateLandVerdicts():         #method for generating the land verdicts
        
        if (positiveProbability > negativeProbability) and (positiveProbability > neutralProbability):    
            sample = "for the foregoing reasons"
            startingSequence = sample
            
            os.chdir('D:\\Education\\UoW\\COURSEWORK AND ASSIGNMENTS\\Year 2\\SDGP\\Prototype\\Land Model Results\\Positive')
            
            char2int = pickle.load(open("landPositivechar2int.pickle", "rb"))
            int2char = pickle.load(open("landPositiveint2char.pickle", "rb"))
            
            characterCount = 300           
            uniqueCharacterCount = len(char2int)
            
            model = Sequential([
                LSTM(128, return_sequences = True, input_shape=(characterCount, uniqueCharacterCount)),
                LSTM(256, return_sequences = True),
                LSTM(512),
                Dense(uniqueCharacterCount, activation="softmax"),
            ])
            
            model.load_weights("positiveResults/verdictland-v1-0.03.h5")
            
        elif (negativeProbability > positiveProbability) and (negativeProbability > neutralProbability):
            sample = "i answer all the questions"
            startingSequence = sample
            
            os.chdir('D:\\Education\\UoW\\COURSEWORK AND ASSIGNMENTS\\Year 2\\SDGP\\Prototype\\Land Model Results\\Negative')
            
            char2int = pickle.load(open("landNegativechar2int.pickle", "rb"))
            int2char = pickle.load(open("landNegativeint2char.pickle", "rb"))
            
            characterCount = 480           
            uniqueCharacterCount = len(char2int)
            
            model = Sequential([
                LSTM(128, return_sequences = True, input_shape=(characterCount, uniqueCharacterCount)),
                LSTM(256, return_sequences = True),
                LSTM(512),
                Dense(uniqueCharacterCount, activation="softmax"),
            ])
            
            model.load_weights("negativeResults/verdictland-v1-0.02.h5")
            
        generatedVerdict = ""
        
        for i in tqdm.tqdm(range(characterCount), "Generating verdict"):       
            X = np.zeros((1, characterCount, uniqueCharacterCount))                  
            
            for t, char in enumerate(sample):
                X[0, (characterCount - len(sample)) + t, char2int[char]] = 1
                
            predictCharacter = model.predict(X, verbose=0)[0]          
            vecToInt = np.argmax(predictCharacter)                   
            intToChar = int2char[vecToInt]                   
            generatedVerdict += intToChar                              
            sample = sample[1:] + intToChar                     
                
        finalVerdict = startingSequence + generatedVerdict
        print(finalVerdict)
        
        result = [
                 {
                     
                  'Generated Verdict ':finalVerdict
                  }
                ]
        
        return (result)   
    
    """
    for key in keywordsInQuery:
        if key in keywords:
            keyword = key
    """        
    keyword = 'child'        
         
    #after checking for the keywords if they are valid we will be generating the verdict for a case
    if keyword == 'murder':
        generateMurderVerdicts()
    if keyword == 'child':
        generateChildVerdicts()
    if keyword == 'commercial':
        generateCommercialVerdicts()  
    if keyword == 'land':
        generateLandVerdicts()
    if keyword == 'employee':
        generateEmployeeVerdicts()
    if keyword == 'contract':
        generateContractVerdicts()     