# Maak een lijst met getallen.
# Schrijf een functie vind_grootste_getal die de grootste waarde uit een lijst teruggeeft.
# Gebruik een for-loop om de grootste waarde te vinden.

lijst_getallen = [1, 7 , 5 , 6 , 88 , 55]
def vind_grootste_getal():
    lijst_getallen.sort()
    lijst_getallen.reverse()
    print(lijst_getallen[0])
vind_grootste_getal()