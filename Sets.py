#sets
print("----------This is the result of set----------")
set1 = {"football","basketball","jingalala","janter-mantar","football"}
set2 = {"jingalala-HuHu","jadumanter","football"}
a = set1
b = set2
print("result is:",a)

#lists on set
print("----------This is the result of list on set----------")
list = ["Aditya Sodha","age is 17","standerd is 11th"]
y = list = set(list)
print("result is:",y)

#adding in set
print("----------This is the result of adding in set----------")
set1.add("jingalala-HuHu")
print("result is:",a)

#removing in set
print("----------This is the result of removing in set----------")
set1.remove("jingalala-HuHu")
print("result is",a)

#checking in set
print("----------This is the result of checking in set----------")
z = "football" in set1
d = "chess" in set1
print("football is presente in set1?:",z)
print("chess is presente in set1?:",d)

#combination of set1 & set2
onlySimilers = set1 & set2
print("result is",onlySimilers)

allchr = set1.union(set2)
print("result is:",allchr)	