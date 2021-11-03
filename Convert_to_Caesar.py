#Author: Jack Spence
#Date: 18/08/2012
#Converts a string with lowercase letters to uppercase while removing the spaces and converting the fullstops to "X".


#The string is taken from the user input
#The outputstring is given a empty value to hold the string. 
#For all the characters in the string from "A" - "Z" convert them to uppercase.
#elif for all characters that are "." convert them to "X".
#Return the outputstring to exit the for loop.


#Defenition 
def convertUpper(str):
    #Take all the lowercase letters and makes them uppercase.
    str = str.upper()
    #Outputstring to hold empty string
    outputstring = ""
    #Finds all the characters in the string
    for ch in str:
        #Determines the range for what to convert to Uppercase, this is from "A" - "Z"
        if ch >= 'A' and ch <= 'Z':
            #Take the string from outputstring and adds the two values together.
            outputstring += ch
        #Finds all the fullstops in the string an converts them to lowercase
        elif ch == '.':   
            outputstring +='X'
    #End For loop
    return (outputstring)
