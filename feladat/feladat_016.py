#feladat_016
# while ciklus III.

folytatja = True
while folytatja:
    print(f'Vidd ki a szemetett!')
    valasz = input('Mondjam még egysze? (i/n): ')
    if valasz == 'n':
        folytatja = False

print(f'Vége a programnak ')