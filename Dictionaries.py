#Dictionaries

dict={"aditya":100,"age":17,"standerd":11,"rank":1}

#simpal printing the values of dictionaries
print("--------showing result of aditya--------")
print("result of aditya is:",dict["aditya"])
print("age of aditya is:",dict["age"])
print("standerd of aditya is:",dict["standerd"])

#check the value is present on dictionaries
a="aditya" in dict
b="height" in dict
print("aditya:",a)
print("height:",b)

#delete the value of dictionarie 
del(dict["rank"])
print("full information of aditya:",dict)