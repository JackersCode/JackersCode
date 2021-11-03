#Author: Jack Spence
#Date: 19/08/2021
##Encrypt_to_Caesar is an encryption and decryption key used to shift characters based on the input from the user using the
#given range from 1-26 to encrypt and then -1 - -26 for decryption. 






#The alphabet is where the script will call from to find the values.
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encryptCaesar(shiftKey, inputString):

    ciphertext = ""   

    # shift value can only be an integer
    while isinstance(int(shiftKey), int) == False:
      # asking the user to reenter the shift value
      shiftKey = input("Please enter your key (integers only!): ")

    shiftKey = int(shiftKey)
  
    for i in inputString:
      if i in alphabet:
        AsciiValue = alphabet.index(i) + shiftKey
        ciphertext += alphabet[AsciiValue % 26]
      else:
        ciphertext += i    
    
    
    return ciphertext