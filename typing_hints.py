x = 4
print(type(4)) # at this moment, x points to an integer

x = "Hello, world"
print(type(x)) # and at this moment, x points to a string

name: str = "world"

def greeting(name: str) -> str:
    return "Hello " + name

print(greeting(name))