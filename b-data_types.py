# type()
print(type(33))  # <class 'int'>
print(type(3.3))  # <class 'float'>

print(type("mina"))  # <class 'str'>

print(type([1, 2, 3, 4, 5]))  # <class 'list'>

print(type((1, 2, 3, 4, 5)))  # <class 'tuple'>

print(type({"one": 1, "two": 2}))  # <class 'dict'>

print(type(2 == 2))  # <class 'bool'>

# variables

myVar = "first var"
print(myVar)

myVar: str = "first var"
print(myVar)

myVar: int = "string int"
print(myVar)

myVar: int = int
print(myVar)

myVar: int = 30
print(myVar)


a, b, c = 1, 2, 3

print(a)  # 1
print(b)  # 2
print(c)  # 3

# 
