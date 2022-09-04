import os
import re
import sys

def isPhoneNumber(string):
    
    matches = re.findall("\d{3}-\d{3}-\d{4}",string) #Regex method for finding all ###-####-####
    length = len(matches)
    # if length == 0:
    #     print("0 match")
    #     return False
    # else:
    #     print(str(len(matches)) + " match(es): " + str(matches)) 
    #     return True
    print(str(len(matches)) + " match(es): " + str(matches)) 
    return length !=0
    
try:
    with open(str(sys.argv[1]),'r') as f:
        text = str(f.readlines())[2:-2]
except:
    print("Can't open provided path in command argument. Openng test.txt file...")
    with open("test.txt",'r') as f:
        text = str(f.readlines())[2:-2]


print(isPhoneNumber(text))
