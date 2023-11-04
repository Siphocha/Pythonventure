import random

chars = "abcdefihgjklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890?^%$#@!*&+_-|<>"
password = ""

Player = False

print("We are using char list = %s \n" % chars)

length = int(input("[*] Input Password Length: "))
while len(password) != length:
    password = password + random.choice(chars)
    if len(password) == length:
        print("password: %s" % password)
        
        Player == False
