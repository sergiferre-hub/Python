#1

x = int(input("Posa la teva edat: "))

if x < 18:
    print("Ets menor d'edat.")
else:
    print("Ets adult.")


#2

num1 = int(input("Posa el primer numero: "))
num2 = int(input("Posa el segon numero: "))
num3 = int(input("Posa el tercer numero: "))

if num1 >= num2 and num1 >= num3:
    print("El numero mes gran es:", num1)
elif num2 >= num1 and num2 >= num3:
    print("El numero mes gran es:", num2)
else:
    print("El numero mes gran es:", num3)


#3

x = int(input("Posa un numero: "))

if x < 0:
    print("El numero es negatiu.")
else:
    print("El numero es positiu.")