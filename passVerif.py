userName = input("please give your name: ")
password = input("Give a proper password: ")
rePassword = input("Re enter the password: ")
temp = 0
wrt = 0

# CHECK FIRST CHAR IS UPPERCASE
if password[0].isupper():
    wrt = wrt+1
else:
    temp = 1
    print("first character can not be in small case")

# CHECK USER NAME IN IT
if userName in password:
    temp = 1
    print("your password can not contain user name")
else:
    wrt = wrt+1

# checking the length
if len(password) >= 8 or len(password) >= 16:
    print(len(password))
    wrt = wrt+1
else:
    temp = 1
    print(len(password))
    print("Your password has be range of 8 to 16")

# for checking both password are same
if password == rePassword:
    wrt = wrt+1
else:
    print("please give same password in both fild")
    temp = 1

# for checking special char
spl = 0
for i in list(password):
    # print(i)
    if i in "[@_!#$%^&*()<>?/|}{~:]":
        spl = spl+1
        break
if spl == 0:
    temp = 1
    print("does not have a special char")

# print(temp)
if temp == 0:
    print("your password is a proper password")
