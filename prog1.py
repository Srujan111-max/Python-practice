print ("Hello,World!")

str1 = "apna_college"
print (str1[:]) # Prints from start to end of the string
print(str1[-10:-1])
print(str1[-1:-10]) # Empty line will come in output for this and no error

str2 = "i am a coder."
print(str2.endswith("er."))
print(str2.capitalize()) # To capitalize the first letter of the string
print(str2) # Here again first letter won't be capital
str2 = str2.capitalize() # To permanently capitalize the first letter and store that in same string name
print(str2)

str3 = "I am learning python from apna_college"
print(str3)
print(str3.replace("a","z"))
print(str3.replace("python","java"))
print(str3)
print() # Prints empty line 

print(str3.find("from"))
print(str3.find("p"))
print(str3.find("Z")) # Returns -1 because -1 i.e., (negative indexing won't exist in strings)
print(str3.find("Q")) # Returns -1 because -1 i.e., (negative indexing won't exist in strings)

print(str3.count("l"))
print(str3.count("am"))
print(str3.count("javascript"))
