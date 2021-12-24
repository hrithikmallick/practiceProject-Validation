password = "hello1234@"
spl = 0
temp = 0
for i in list(password):
    # print(i)
    if i in "[@_!#$%^&*()<>?/|}{~:]":
        spl = spl+1
        break
if spl == 0:
    temp = 1
    print("does not have a special char")
if temp == 0:
    print("pass does have a special char")
