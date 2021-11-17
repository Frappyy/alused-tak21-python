name = input("Mis su nimi on?: ")

print("Tere ", name, "!", sep='')

location = input("Kus sa elad?: ")

if location == "Saaremaa":
    print("Tere saarlane!")

age = int(input("Kui vana sa oled?: "))

if age < 18:
    print("Sa oled liiga noor, et autot juhtida.")
elif age == 18:
    print("Õnnitlused täisealiseks saamisel!")
elif age > 18:
    print("Sa oled piisavalt vana, et autoga sõita.")   