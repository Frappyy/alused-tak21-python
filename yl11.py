uInput = input("Sisesta midagi: ")
midChar = uInput[len(uInput)//2]

uInput.replace(" ", "")

def evenOdd(int):
    if (int % 2) == 0:
        return False
    else:
        return True

if len(uInput) >= 7 and evenOdd(len(uInput)):
    print(uInput[len(uInput)//2-1:len(uInput)//2+2])
else:
    print("Pole piisavalt tähti(min 7) või arv tähti on paarisarv!")