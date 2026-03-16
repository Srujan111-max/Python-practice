# problem 1
dict = {
    "cat" : "A small animal",
    "table" : ("list of facts & figures", "A piece of furniture")
}
print (dict)

# problem 2 
set1 = {
    "python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"
}
set2 = {
    "python", "java", "C++", "javascript", "C"
}
print ("The number of classsrooms needed for each subjects is :", len(set2.union(set1)))

# or problem 2 can be done by
list1 = ["python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"]
list2 = set(list1)
print(list2)
print("The number of classrooms needed for each subjects is :", len(list2))

# or problem 2 can be done by
group1 = {
 "python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"   
}
print ("The number of classrooms needed for each subjects is :", len(group1)) 