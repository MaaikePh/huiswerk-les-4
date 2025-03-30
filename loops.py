# Tafels

# Schrijf een programma dat de tafel van een getal afdrukt.
# De gebruiker voert een getal in en het programma drukt de tafel van dat getal af.
# De tafel van 7 ziet er bijvoorbeeld als volgt uit:
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 7 x 10 = 70


# Probeer het eerst zonder loop,

tafel = int(input('Vul hier het cijfer in waar je de tafel van wil zien: '))
print(tafel, 'x 1 =' ,tafel * 1)
print(tafel, 'x 2 =' ,tafel * 2)
print(tafel, 'x 3 =' ,tafel * 3)
print(tafel, 'x 4 =' ,tafel * 4)
print(tafel, 'x 5 =' ,tafel * 5)
print(tafel, 'x 6 =' ,tafel * 6)
print(tafel, 'x 7 =' ,tafel * 7)
print(tafel, 'x 8 =' ,tafel * 8)
print(tafel, 'x 9 =' ,tafel * 9)
print(tafel, 'x 10 =' ,tafel * 10)

# Probeer het nu met een loop.

tafel1 = int(input('Vul hier het cijfer in waar je de tafel van wil zien: '))

for cijfer in range(1, 11):
    print(tafel1, "x", cijfer, "=", tafel1 * cijfer)


# --------------------------------------------------------------------------------------------

# Optellen
# Schrijf een programma dat de som van alle getallen tot een bepaalde limiet berekent.

# Bijvoorbeeld: de som van alle getallen tot 3 is 6 (1 + 2 + 3 = 6)

# limiet = 6
#
# for cijfer in range(1,10):
#     if cijfer == 6 :
#         break
#     print(cijfer)

limiet = int(input('Voer een limiet in: '))
cijfer = 1
som = 0

while cijfer <= limiet:
    som += cijfer
    cijfer += 1
print("De som van getallen tot", limiet, "is", som)

# --------------------------------------------------------------------------------------------

# Dit is een klassieke programmeeroefening die vaak wordt gebruikt in sollicitatiegesprekken.
# FizzBuzz

# Schrijf een programma dat de getallen van 1 tot 100 afdrukt.
# Maar voor veelvouden van drie, druk "Fizz" af in plaats van het getal.
# En voor veelvouden van vijf, druk "Buzz" af.
# Voor veelvouden van zowel drie als vijf, druk "FizzBuzz" af.

for teller in range(1,101):
    if teller % 3 == 0 and teller % 5 == 0:
        print("FizzBuzz")
    elif teller % 3 == 0:
        print("Fizz")
    elif teller % 5 == 0:
        print("Buzz")
    else:
        print(teller)


# --------------------------------------------------------------------------------------------


# Fibonacci-reeks

# De eerste twee getallen van de Fibonacci-reeks zijn 0 en 1.
# Elk volgend getal is de som van de twee voorgaande.
# De eerste 10 getallen van de Fibonacci-reeks zijn:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# 0 + 1 = 1
# 1 + 1 = 2
# 1 + 2 = 3
# 2 + 3 = 5
# 3 + 5 = 8
# 5 + 8 = 13
# 8 + 13 = 21
# 13 + 21 = 34

i = int(input("Hoeveel Fibonacci-getallen wil je zien? "))
#
# # De eerste twee getallen van de Fibonacci-reeks zijn 0 en 1
a = 0
b = 1

# Eerst drukken we de eerste twee getallen af

print(a)
print(b)

# Vervolgens berekenen we de volgende getallen en drukken ze af

for x in range(2, i):
    c = a + b
    print(c)
    a = b
    b = c