x = input("Sisesta esimene arv (x): ")
y = input("Sisesta teine arv (y): ")
z = input("Sisesta kolmas arv (z): ")

if x > y and x > z:
    print("Suurem number on X:", x)
elif y > x and y > z:
    print("Suurem number on Y:", y)
elif z > x and z > y:
    print("Suurem number on Z:", z)
