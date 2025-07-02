import random
chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYA!$%&'()-^~|¥@`+:*?><_"
lenght=int(input("enter your password length: "))
password=""

for a in range (lenght):
    password+=random.choice(chars)
print("This is your password")
print(password)
