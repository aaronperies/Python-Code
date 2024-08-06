number = int(input("Enter a number between 0 and 100: "))

if number < 0 or number > 100:
    print("Invalid")
else:
    if number >= 75:
        print("A pass")
    else:
        print("Fail")
