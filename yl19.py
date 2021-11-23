from typing import Counter


uInput = input("Sisestage lause või sõna: ")
chars = "AaEeIiOoUuÕõÄäÖöÜü"

def check_vow(string, chars):
    final = [each for each in string if each in chars]
    print(len(final))

check_vow(uInput, chars)