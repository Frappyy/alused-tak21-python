favFruits = ["Õun", "Banaan", "Kiivi"]

print("Esimene puuvili:", favFruits[0])

favFruits.append("Pirn")

print("Viimane puuvili:", favFruits[len(favFruits)-1])

favFruits[1] = "Mandariin"
print(favFruits)

favFruits.remove("Mandariin")
print(favFruits)

if "Õun" in favFruits:
    print("Õun on olemas!")
else:
    print("Õuna pole olemas.")

print("Listis on", len(favFruits), "elementi.")

favFruits.reverse()
favFruits.sort()
print(favFruits)