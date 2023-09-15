# feladat_001
"""
kérjük be a billenytyűzetről a nevünket ki a képernyőre!
A billentyűzetről mindig szöveget (string-et) olvasunk be!
type(változó)
"""
'''
nev = input("kérek egy nevet: ")
print( f"A megadott név a következő: {nev}") 
'''

vnev = input("Kérek egy vezetéknevet: ")
knev = input("Kérek egy keresztnevet: ")
print(f"A megadott név a következő: {vnev} {knev}")

print(f"A vnév változó tipusa: {type(vnev)}")
print(f"A knév változó tipusa: {type(knev)} ")
