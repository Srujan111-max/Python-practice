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
    
#5 Find the number in the tuple
list1 = (1,4,9,16,25,36,49,64,81,100)
x = int(input("Enter the number to find in list: "))
i = 0
print(len(list1))

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
