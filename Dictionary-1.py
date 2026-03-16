info = {
    "Name":"Srujan S Govinagidad",
    "subjects_scr" : {
        "phy" : 89,
        "chem" : 96,
        "math": 93
    }
    }
print(len(info))
print(list(info.keys()))
print(info.keys())
print(info.items())
print(info)
list = list(info)
print (list[0])
print(info.get("subjects_scr"))

mydict =  {"Roll number" : 1234567890}
info.update(mydict)
print (info)
