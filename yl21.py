import random

rNum = random.randrange(0, 100)

while(True):
    uInput = int(input("Arva ära mis numbri see valis: "))

    if uInput == rNum:
        print("Valisid õigesti!")
        break
    elif uInput > rNum:
        print("Vihje: sinu arvatud number on suurem kui arvuti oma.")
    else:
        print("Vihje: sinu arvatud number on väiksem kui arvuti oma.")