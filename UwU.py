def addCuteness(a):
    b = a.replace("L", "W")
    b = b.replace("l", "w")
    b = b.replace("R", "W")
    b = b.replace("r", "w")
    b = b.replace(".", " UwU.")
    b = b.replace("?", " OwO?")
    return (b.replace("!", " OwO!"))
print(addCuteness(input("UwU: ")))