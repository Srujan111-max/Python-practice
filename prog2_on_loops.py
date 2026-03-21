#1 Printing items in the list using for
Names = ("Apple","Papaya","Srujan",58,7)
for i in Names:
    print (i)
print ("The end")    

#2 Printing the sepration of a word by letters
Word = "SRUJAN S GOVINAGIDAD"
for i in Word:
    print(i, end = ",")

#3 Printing the sum upto n number of integers using for
n = int(input("enter the number: "))
sum = 0
for i in range (n+1):
    sum = sum + i
print ("the Sum of numbers from 1 to",n , "is:", sum)    

#4 Counting the numbers of letters in a name 
Name = input ("Enter the the name: ")
for i in range (len(Name)):
    print("the ",i,"letter of Name is",Name[i])

# Finding element in tuple using for
list = (1,4,9,16,25,36,49,64,81,100,81)
n = int(input("enter element to search: "))
index = 0
for i in list:
    if (n == i):
        print("element found at index:",index)
        index += 1
    index += 1
if (n == i):
    None
else:
    print("Not found")

# Fatorial of n numbers using for
m = int(input("enter the number: "))
mul = 1
for i in range(m,1,-1):
    mul = mul * i
print(mul)
    
#5 Find the number in the tuple using while
list1 = (1,4,9,16,25,36,49,64,81,100)
x = int(input("Enter the number to find in list: "))
i = 0
print(len(list1))
while i < len(list1):
    if (x == list[i]):
        print(" Found at index",i)
    i += 1

# Use of break statement in a while loop
i = 1
while i <= 5:
    print (i)
    if (i == 3):
        break
    i += 1
print("Loop terminated.")

# Use of continue statement
i = 1
while i <= 5:
    if (i == 3):
        print ("the", i,"rd iteration is skipped")
        i += 1
        continue
    print(i)
    i += 1

i = 0
while i <= 10:
    if (i%2 == 0): # Prints ODD numbers from 1-10
        i += 1
        continue
    print (i)
    i += 1
print("\n")
j = 0
while j <= 10:
    if (j%2 != 0): # Prints EVEN numbers from 1-10
        j += 1
        continue
    print (j)
    j += 1

# Sum of n numbers using while 
n = int(input("enter the number: "))
i = 0
sum = 0
while i <= n:
    sum = sum + i
    i += 1
print(sum)
