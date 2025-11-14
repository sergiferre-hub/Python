def calcular_area_quadrat():
#1
    from time import sleep
    print ("Posa el numero de l'altura del quadrat:")
    y = (input())

    print ("L'area del quadrat es :", int(y) * int(y))

    sleep(1)

def operacions_basiques():
#2
    from time import sleep
    print ("Posa dos numeros:")
    x = int(input())
    y = int(input())

    print ("La suma es :", x + y)
    print ("La resta es :", x - y)
    print ("La multiplicacio es :", x * y)
    print ("La divisio es :", x / y)

    sleep(1)

def fer_frase():
#3
    from time import sleep
    print ("Posa 3 paraules per fer una frase:")
    a = input()
    b = input()
    c = input()

    print ("La frase es:", a, b, c)

    sleep(1)

def operacions_basiques_amb_coma():
#4
    from time import sleep
    x = float(input("Posa un numero amb coma:"))
    y = float(input("Posa un altre numero amb coma:"))

    print ("La suma es:", int(x + y))
    print ("La resta es:", int(x - y))

    sleep(1)

def comparar_anys():
#5
    from time import sleep
    x = int(input("Posa la teva edat: "))

    if x < 18:
        print("Ets menor d'edat.")
    else:
        print("Ets adult.")

    sleep(1)

def numero_mes_gran():
#6
    from time import sleep
    num1 = int(input("Posa el primer numero: "))
    num2 = int(input("Posa el segon numero: "))
    num3 = int(input("Posa el tercer numero: "))

    if num1 >= num2 and num1 >= num3:
        print("El numero mes gran es:", num1)
    elif num2 >= num1 and num2 >= num3:
        print("El numero mes gran es:", num2)
    else:
        print("El numero mes gran es:", num3)

    sleep(1)



def numero_positiu_o_negatiu():
#7
    from time import sleep
    x = int(input("Posa un numero: "))

    if x < 0:
        print("El numero es negatiu.")
    else:
        print("El numero es positiu.")

    i = 2

    for i in range(2, 201, 2):
        print(i)

    sleep(1)

def comprovar_nota_10():
#8
    from time import sleep
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

    sleep(1)

def comprovar_nombres_negatius():
#9
    from time import sleep
    for i in range(10):
        msg = f"introdueix el nombre { i + 1 } de 10: "
        num = float(input(msg))
        if num < 0:
            hi_ha_negatiu = True
    if hi_ha_negatiu:
        print("Hi havia algun nombre negatiu.")
    else:
        print("No hi havia cap nombre negatiu.")
    
    sleep(1)


while True:
    print("1. Calcular Àrea del Quadrat")
    print("2. Operacions Bàsiques (+, -, *, /)")
    print("3. Fer Frase amb 3 paraules")
    print("4. Operacions amb Coma (Float)")
    print("5. Comparar Edat (Menor/Adult)")
    print("6. Trobar el Número Més Gran de 3")
    print("7. Número Positiu/Negatiu i Números Parells (Fins a 200)")
    print("8. Comprovar Nota 10 (Bucle While)")
    print("9. Comprovar Nombres Negatius (Bucle For)")
    print("s. Sortir del Programa")
    
    opcio = input("Selecciona una opció (1-9 o s): ")

    match opcio:
        case '1':
            calcular_area_quadrat()
        case '2':
            operacions_basiques()
        case '3':
            fer_frase()
        case '4':
            operacions_basiques_amb_coma()
        case '5':
            comparar_anys()
        case '6':
            numero_mes_gran()
        case '7':
            numero_positiu_o_negatiu()
        case '8':
            comprovar_nota_10()
        case '9':
            comprovar_nombres_negatius()
        case 's':
            print("Programa finalitzat. Gràcies per utilitzar-lo!")
            break 
            
        case _:
            print("ERROR: Opció no vàlida. Si us plau, tria un número de l'1 al 9 o 's' per sortir.")