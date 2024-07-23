import random

print("Welcome to random password genrator application")

print("Please enter your password Genration details here...")

randomchars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+="

nbrofpswrd = int(input("Please Enter How many Password you want = "))

pswdlimt  = int(input("Please enter your password character limit = "))



for i in range(nbrofpswrd):
    pwd = ""
    for charts in range(pswdlimt):
        pwd = pwd + random.choice(randomchars)
    print(pwd)