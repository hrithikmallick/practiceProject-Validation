
email = "hrithik@gmail.in"
lenGth = len(email)
apt = email.find("@")
dot = email.find(".", apt)
print(dot, apt)
print(dot-apt)
if dot-apt <= 4:
    print("not valid")

print(lenGth)
