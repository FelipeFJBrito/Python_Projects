#functions with input
def greet():
    print("Hello")
    print("How do you do")

greet()


def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}")

greet_with_name("Felipe")


#functions with more then one input

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("Felipe", "Vancouver")

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with(name = "elipe", location="Vancouver")