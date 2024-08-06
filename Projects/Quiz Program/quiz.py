#create dictionary with questions
qs_as = {
    "Q1": {
        "question": "What is the capital of England ?",
        "answer": "London"
        },
    "Q2": {
        "question": "What is the capital of Germany ?",
        "answer": "Berlin"
        },
    "Q3": {
        "question": "What is the capital of Russia ?",
        "answer": "Moscow"
        },
    "Q4": {
        "question": "What is the capital of Australia ?",
        "answer": "Sydney"
        },
    "Q5": {
        "question": "What is the capital of Canada ?",
        "answer": "Ottawa"
        }
    }

print("Welcome to the Capital Cities Quiz!\n")
user_score = 0

for key, value in qs_as.items():
    print(value['question'])
    answer = input("Your answer: ")

    #we are converting both strings to lower case to avoid case sensitivity issues
    if answer.lower() == value['answer'].lower():
        print("Your answer is correct!")
        user_score+=1
        print("Your score is:", user_score, "\n")

    else:
        print("Your answer is wrong! The correct answer:", value['answer'])
        print("Your score is:", user_score, "\n")

print("You have completed the quiz!")
print("You got", user_score, "out of", len(qs_as))
print("Score percentage is:", int((user_score/len(qs_as))*100), "%")
    
