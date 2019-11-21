helloWorld = ""


def World():
    global helloWorld
    return helloWorld.__new__


def Hello():
    global helloWorld
    helloWorld += "Hello World!"
    print(helloWorld)
