userName = input("please give your name: ")
# emailName = input("please give your proper email address ")
password = input("Give a proper password: ")
rePassword = input("Re enter the password: ")
temp = 0
wrt = 0


if password[0].isupper():
    wrt = wrt+1
else:
    temp = 1
    print("first character can not be in small case")


if userName in password:
    temp = 1
    print("your password can not contain user name")
else:
    wrt = wrt+1


if len(password) >= 8 or len(password) >= 16:
    print(len(password))
    wrt = wrt+1
else:
    temp = 1
    print(len(password))
    print("Your password has be range of 8 to 16")


if password == rePassword:
    wrt = wrt+1
else:
    print("please give same password in both fild")
    temp = 1


for i in list(password):
    spl = 0
    if i in "[@_!#$%^&*()<>?/|}{~:]":
        spl = spl+1
        break
    if spl > 1:
        temp = 1


# print(temp)
if temp == 0:
    print("your password is a proper password")
