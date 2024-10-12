# We gaan aan de gebruiker een aantal instructies vragen en op basis daarvan tekenen.
# - Maak eerst een lege lijst waar de stappen in zullen komen.
# - Maak een oneindige lus:
#     - Vraag een stap aan de gebruiker
#     - Als het gelijk is aan “stop”, breek uit de lus.
#     - Anders, voeg het toe aan de lijst met stappen.
# - Itereer over de stappenlijst om te tekenen

import turtle



stappen = []
while True:
    int = input("wat moet de figuur doen")
    if int == "stop" :
        break
    else:
        stappen.append(int)


for item in stappen:
    if item == "o":
        turtle.forward(50)

