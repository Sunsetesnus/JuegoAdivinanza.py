import random


numero_secreto = random.randint(1,101)
adivinado = False

print("Bienbenido al world de adibinar lo que no importa en la vida")

while not adivinado:
    entrada = input("introduce un numero del 1 al 100: ")
    numero = int(entrada)

    if numero == numero_secreto:
        print("Coronaste")
        adivinado = True
    elif numero < numero_secreto:
        print("el # es > al ingresado")
    else:
        print("el numero es menor al ingresado")