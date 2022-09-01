import os
import re
import sys

def isPhoneNumber(string):
    # if len(string) != 12:
    #     return False
    x=re.search("\d{3}-\d{3}-\d{4}",string)
    matches = re.findall("\d{3}-\d{3}-\d{4}",string)
    length = len(matches)
    if length == 0:
        print("0 match")
        return False
    else:
        print(str(len(matches)) + " match(es): " + str(matches)) 
        return True
print(sys.argv)
print("length: " + str(len(sys.argv)))

try:
    with open(str(sys.argv[1]),'w') as f:
        file = f
        text = str(file.readlines())[2:-2]
except:
    print("Can't open provided path in command argument. Openng test.txt file...")
    file = open("test.txt",'r')
    text = str(file.readlines())[2:-2]

print(text)

print(isPhoneNumber(text))
