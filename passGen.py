import random


def generatepass(rng):
    passw = ""
    strng = "ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$&%-_" + \
        "abcdefghijklmnopqrstuvwxyz0123456789@#$&%-_"
    i = 0
    # rng = random.randrange(8, 16)
    while i <= rng:
        i += 1
        rand = random.randrange(0, len(strng)-1)
        passw += strng[rand]

    print('\nPlease copy your secure password: \n\n\t' +
          passw+'\n\n!!!  Copy it then use it  !!!\n')
    return passw


# try:
#     rng = int(input("please give the length of password:- "))
#     print(generatepass(rng))
# except:
#     print("length always in int")

# UNCOMMENT IT IF USING NON MODULE WISE
