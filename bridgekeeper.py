def put():
    print("die")
def go():
    print("go on")
    
name = input("what is your name")
quest = input ("what is your quest")

if name == "lancelot":
    color = input("what is your favorite color")
    if color == "blue":
        go()
    else:
       put()
elif name =="robin":
    capital = input("what is the capital of assyria?")
    if capital == "assur" or capital =="ashur":
        go()
    else:
        put()
