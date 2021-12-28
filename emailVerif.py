def emailVerifier(email):
    lenEm = len(email)
    print("length of your email is :- ", lenEm)

    temp = 0
# CHECKING @ IN EMAIL
    if (email.find('@') == -1):
        print("@ missing")
        temp = temp+1

    apt = email.find("@")
    dot = email.find(".", apt)

# CHECKING DOMAIN IN EMAIL
    if (apt != -1):
        if dot < apt:
            print("invalid check domain again")
            temp = temp+1
    else:
        if email.find(".") == -1:
            print(". is also missing")
    if lenEm-dot <= 2:
        temp = temp+1
        print("invalid domain")
# CHECKING MAIL SERVER PROVIDER
    if dot-apt <= 4:
        print("mail server is missing")
        temp = temp+1
# DELETE USING VARIBALE TO CLEAR THE SPACE
    del lenEm
    del apt
    del dot

# ATLAST RESULT
    if temp == 0:
        print("It is a vaild email")
        return True
    else:
        return False


# email = input("Enter your email:- ")
# tmp = emailVerifier(email)
# print(tmp)

# UNCOMMENT IT FOR IF USING NON MODULE WISE
