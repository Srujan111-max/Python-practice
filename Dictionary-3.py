#1 enter 3 subjects from user and store them in a dictionary 
marks = {}
sub1 = int(input("Enter the marks of chemistry subject: "))
sub2 = int(input("Enter the marks of physics subject: "))
sub3 = int(input("Enter the marks of maths subject: "))
marks2 = {
    "chem" : sub1,
    "phy" : sub2,
    "math" : sub3
}
marks.update(marks2)
print(marks)

#2 Save both 9 and 9.0 in set
set1 = {
    ("int" , 9),
    ("float" , 9.0)
}
print (set1)