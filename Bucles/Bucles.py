#1

i = 2

for i in range(2, 201, 2):
    print(i)


#2

El_Deu = False
nota = int(input("Introdueix una nota entre l'1 i el 10 o -1 per acabar: "))

while nota != -1:
    if nota == 10:
        El_Deu = True
        print("Hi ha un 10")
    else:
        print("No hi ha cap 10")
    nota = int(input("Introdueix una nota entre l'1 i el 10 o -1 per acabar: "))
if not El_Deu:
    print("No hi ha hagut cap 10")
else:
    print("Hi ha hagut un 10")

#3
for i in range(10):
    msg = f"introdueix el nombre { i + 1 } de 10: "
    num = float(input(msg))
    if num < 0:
        hi_ha_negatiu = True
if hi_ha_negatiu:
    print("Hi havia algun nombre negatiu.")
else:
    print("No hi havia cap nombre negatiu.")