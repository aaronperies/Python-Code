def wordReplace(sentence):
    print(sentence)
    word_to_replace = input("Enter the word you want to replace: ")

    if(word_to_replace in sentence):
        replacing_word = input("Enter the word you want to use: ")
        print(sentence.replace(word_to_replace, replacing_word))
    else:
        print("\nThe word you entered is not in the sentence")
        wordReplace(sentence + "\n")

    
wordReplace("Hello my name is Aaron")
