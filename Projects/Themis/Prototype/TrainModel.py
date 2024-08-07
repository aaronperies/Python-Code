import numpy as np                           #used to perform vectorization
import os                                    #used in accessing folders and other directories while executing
import pickle                                #storage medium such as json
from keras.models import Sequential          #type of model we'll be using
from keras.layers import Dense, LSTM         #different types of layers we'll be using
from keras.callbacks import ModelCheckpoint  #used to create checkpoints after each epoch has been run
from string import punctuation               #used to remove all the punctuation marks in the text corpus

class TrainModel:
    
    def trainModel(directory, filename, pickle1, pickle2, filepath):  #this directory variable is used to set the directory of the folder where we will iterate through the PDF documents
        
        os.chdir(directory)     #switches working directory to the one passed in parameters
        
        txtFileObj = open (filename, encoding = "utf-8").read()   #reads the textfile containing the verdicts
        txtFileObj = txtFileObj.lower().replace("\n\n", "\n")                 #convert to lower case and double lines
        txtFileObj = txtFileObj.translate(str.maketrans("", "", punctuation)) #remove punctuation marks from text
                
        uniqueChars = ''.join(sorted(set(txtFileObj)))  #identifies each unique character in the text
        uniqueCharCount = len(uniqueChars)              #number of unique characters
         
        #how to convert characters to integers and vice versa while storing them in a dictionary was learned from (https://www.thepythoncode.com/article/text-generation-keras-python)
        char2int = {c: i for i, c in enumerate(uniqueChars)}   # dictionary that converts characters to integers
        int2char = {i: c for i, c in enumerate(uniqueChars)}   # dictionary that converts integers to characters
        
        #from json, text, csv and pickle, pickle was the most used by other individuals for their personal projects
        pickle.dump(char2int, open(pickle1, "wb"))    # save these dictionaries for later generation
        pickle.dump(int2char, open(pickle2, "wb"))
        
        #parameters (how to configure these parameters in the model was learned from the source mentioned above as well)
        sequenceLength = 120 #120 for larger corpus, justification at (https://www.quora.com/What-is-a-sequence-length-of-the-RNN-If-I-use-a-sequence-length-of-1-is-that-a-problem-What-does-it-means)
        step = 1        #step size justification (http://numahub.com/articles/machine-learning-concept-step-size)
        batchSize = 96  #96 for larger corpus
        epochs = 40     #40 for larger corpus
        sentences = []  
        y_train = []
        
        for i in range(0, len(txtFileObj) - sequenceLength, step):
            sentences.append(txtFileObj[i: i + sequenceLength])
            y_train.append(txtFileObj[i+sequenceLength])
        
        # vectorization, array with desired parameters populated with zeros
        X = np.zeros((len(sentences), sequenceLength, uniqueCharCount))
        y = np.zeros((len(sentences), uniqueCharCount))
        
        for i, sentence in enumerate(sentences):
            for t, char in enumerate(sentence):
                X[i, t, char2int[char]] = 1
                y[i, char2int[y_train[i]]] = 1
                
        print("X shape = ", X.shape)
        print("y shape = ", y.shape)
        
        # building the model
        # after attempting to train a text generating model, I found a decent configuration for the layers
        # to work in the best way to produce a meaningful verdict
        model = Sequential([
            LSTM(128, return_sequences = True, input_shape=(sequenceLength, uniqueCharCount)),
            LSTM(256, return_sequences = True),
            LSTM(512),
            Dense(uniqueCharCount, activation="softmax"),
        ])
        
        model.summary()     #displays the models details before beginning the training process such as the layer details and what the outputs will look like
        model.compile(loss = "categorical_crossentropy", optimizer = "adam", metrics = ["accuracy"])
        #the reason for choosing adam as my optimizing algorithm is justified at (https://towardsdatascience.com/types-of-optimization-algorithms-used-in-neural-networks-and-ways-to-optimize-gradient-95ae5d39529f)
        
        # make results folder if does not exist yet
        if not os.path.isdir(filepath):
            os.mkdir(filepath)
            
        # save the model in each epoch
        checkpoint = ModelCheckpoint(filepath + "/verdictland-v1-{loss:.2f}.h5", verbose = 1)
        model.fit(X, y, batch_size = batchSize, epochs = epochs, callbacks = [checkpoint])
        
        
    trainModel('D:\\Education\\UoW\\COURSEWORK AND ASSIGNMENTS\\Year 2\\SDGP\\Prototype\\ChildVerdicts', 'negativeChildVerdicts.txt', 'negativeChildCharToInt.pickle', 'negativeChildIntToChar.pickle', 'negativeResults')   