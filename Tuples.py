
steden = ("Amsterdam", "Rotterdam", "Utrecht", "Den Haag", "Eindhoven", "Groningen")
# Loop door de tuple en print elk element afzonderlijk

for stad in steden:
    print(stad)

# --------------------------------------------------------------------------------------------

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Combineer de twee tuples tot één nieuwe tuple

tuple3 = tuple1 + tuple2
print(tuple3)

# --------------------------------------------------------------------------------------------


# Definieer een tuple met verschillende soorten gegevens (bijvoorbeeld getallen, strings, booleans, etc.)


# Print enkele elementen van de tuple namelijk het eerste, een subset (vanaf index 2 tot index 5) en het laatste element

tuple_gegevens = (18, 'juli', True, 1996, 'verjaardag', 'hoera')

print(tuple_gegevens[0])
print(tuple_gegevens[2:5])
print(tuple_gegevens[-1])

# --------------------------------------------------------------------------------------------


# Maak een tuple met een naam en een leeftijd


# Pak de gegevens uit de tuple en sla ze op in afzonderlijke variabelen (Wat gebeurt er als je de variabelen in de verkeerde volgorde definieert?)


# Print de uitgepakte variabelen

tuple_persoon = ('Maaike', 28)

naam = tuple_persoon[0]
leeftijd = tuple_persoon[-1]

print(f"Dit is {naam} en de leeftijd is {leeftijd}.")

# naam, leeftijd = tuple_persoon
# print("Naam:", naam)
# print("Leeftijd:", leeftijd)