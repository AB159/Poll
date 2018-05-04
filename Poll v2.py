'''
Poll v 2.2
By Alex 5/1/2018
'''
import ast
names = {}
try:    
    file = open("file.txt", "r")
    names = file.read()
    names = ast.literal_eval(names)
    file.close()
except:
    names = {}

while True:
    name = input(str("Type in your name/Type quit to see the average "))
    if name in names:
        print("Already have that name")
        continue
    if name == "quit":
        print("Average is " + str(sum(names.values()) / len(names)))
        break
    if len(name) < 1:
        print("You have to type something!")
        continue
    if len(name) > 0:
        while True:
            answer = input(str("How many siblings do you have?"))
            try:
                answer = int(answer)
                names[name] = answer
                break
            except:
                print("I only take numbers!")
    file = open("file.txt", "w")
    file.write(str(names))
    file.close()
