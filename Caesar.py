#Author: Jack Spence
#Date: 19/08/2021
#Caesar.py is the front end API that calls all the functions for them to be used together. 



#From Convert_to_Caesar the convertUpper defenition is imported
#From Encrypt_to_Caesar the encryptCaesar is imported
#The user is then asked to enter the plaintext they would like to have encryted
#The user is then asked for the shiftKey, the value that will determine how many characters will be shifted by.
#The import sys will make the program run on the command line. 

import sys 

from Convert_to_Caesar import convertUpper
from Encrypt_to_Caesar import encryptCaesar

try:
    shiftKey = int(sys.argv[1])
    plaintext = str(sys.argv[2])
    print(str(shiftKey), str(plaintext))
except: 
    plaintext = input("Please enter your plaintext: ")
    shiftKey = input("Please enter your key: ")

st1 = convertUpper(plaintext)

st2 = encryptCaesar(shiftKey, st1)

print(st2)