def email_slicer():
    email = input("Enter the email: ")

    if ('@' and '.' not in email):
        print("You have entered an invalid value, try again!\n")
        email_slicer()
    else:
        (username, domain) = email.split("@")
        (domain, extension) = domain.split(".")
        print("Username:", username)
        print("Domain:", domain)
        print("Extension:", extension)

