def emailVerifier(email):
    lenEm = len(email)
    print("length of your email is :- ", lenEm)
    del lenEm
    temp = 0
# CHECKING @ IN EMAIL
    if (email.find('@') == -1):
        print("@ missing")
        temp = temp+1

    apt = email.find("@")
    dot = email.find(".")
# CHECKING DOMAIN IN EMAIL
    if (email.find('@') != -1):
        if email.find(".", apt) < email.find("@"):
            print("invalid check domain again")
            temp = temp+1
    else:
        if email.find(".") == -1:
            print(". is also missing")
# CHECKING PROVIDER
    if (dot-apt) == 1:
        print("provider is missing")
        temp = temp+1

    del apt
    del dot

# ATLAST RESULT
    if temp == 0:
        print("It is a vaild email")


email = input("Enter your email:- ")

# email = "hrithik.mallick20@gmail.com"
emailVerifier(email)
