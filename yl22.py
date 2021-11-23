import random
import os

kpk = ["kivi", "paber", "käärid"]
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

while(True):
    cInput = random.choice(kpk)
    uInput = input("Vali kivi, paber või käärid: ")

    clearConsole()
    if cInput == uInput:
        print("Viik")
    else:
        if cInput == "kivi" and uInput == "paber":
            print("Sina võitsid! Arvuti valis", cInput)
        elif cInput == "kivi" and uInput == "käärid":
            print("Sina kaotasid! Arvuti valis", cInput)
        elif cInput == "paber" and uInput == "käärid":
            print("Sina võitsid! Arvuti valis", cInput)  
        elif cInput == "paber" and uInput == "kivi":
            print("Sina kaotasid! Arvuti valis", cInput)
        elif cInput == "käärid" and uInput == "kivi":
            print("Sina võitsid! Arvuti valis", cInput)  
        elif cInput == "käärid" and uInput == "paber":
            print("Sina kaotasid! Arvuti valis", cInput)
              
    