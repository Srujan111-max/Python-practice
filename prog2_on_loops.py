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
while i < len(list1):
    if (x == list1[i]):
        print("Found at index: ",i)
    i += 1
