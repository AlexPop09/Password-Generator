# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 21:37:52 2022

@author: alex
"""
import string
import random


## characters to generate password 
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()<>?|/+_-")
while 1:
    password_count=int(input("Enter number of passwords: "))
    ## length of password from the user
    password_len=int(input("Enter passwords length: "))
    for i in range(0,password_count):
        password=" "
        for i in range(0,password_len):
            password_characters=random.choice(characters)
            password=password+password_characters
            
        print("Here is your random password: ",password)
        
        