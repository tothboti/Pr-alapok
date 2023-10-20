# feladat_015

'''
Kérjük be a vezeték és keresztnevünket 
Irassuk ki eljárás segítségével nevunkent
pl: 
be:
'''

vezeteknev = input('Kérem a vezetékneved: ')
keresztnev = input('Kérem a keresztneved: ')

def nevf(vnev,knev):
    nevem = vnev + " " + knev
    return nevem 

print(f" A nevem: {nevf(vezeteknev,keresztnev)}")

