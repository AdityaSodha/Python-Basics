#List
list = ["Aditya Sodha","age is 17","standerd is 11th"]
print("--------result of 0--------")
print("result is:",list[0])

print("--------result of 1--------")
print("result is:",list[1])

print("--------result of 2--------")
print("result is:",list[2])

print("--------result of extending list--------")
list.extend(["rank is 1st"])
print("result is:",list)

print("--------result of replacing list--------")
list[0]="aditya"
print("result is:",list)

print("--------result of deleteing list--------")
del(list[0])
print("result is:",list)

#split
print("--------result of split--------")
a = "aditya","sinh","Sodha".split(",")
print("result is:",a)