#1

i = 2

for i in range(2, 201, 2):
    print(i)


#2

El_Deu = False
nota = int(input("Introdueix una nota entre l'1 i el 10 o -1 per acabar: "))

while nota == 10:
    El_Deu = True
    print("Hi ha un 10")
    nota = int(input("Introdueix una nota entre l'1 i el 10 o -1 per acabar: "))
else:
    print("No hi ha cap 10")
    while nota != -1 and not El_Deu:
     print("No hi ha cap 10")
     nota = int(input("Introdueix una nota entre l'1 i el 10 o -1 per acabar: "))

while nota == -1:
    print("Fi del programa")