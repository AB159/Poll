'''
Poll v 0.9
By Alex 4/27/2018
'''
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
    if len(name) > 1:
        while True:
            answer = input(str("How many siblings do you have?"))
            try:
                answer = int(answer)
                names[name] = answer
                break
            except:
                print("I only take numbers!")
