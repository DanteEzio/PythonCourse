# Crear el juego de piedra papel o tijera
# Pedirle al jugador que eliga su opcion
# Hacer que la computadora eliga una accion
# Crear los casos diferentes para cada una de las opciones que elija el usuario y la computadora
# Si el usuario elije piedra y la computadora también, es empate
# Si la computadora eligio papel, gana la computadora
# Si la computadora eligio tijeras, gana el usuario

from random import randint

pc = randint(1,3)   


name = input('Input your name: ')
print('Hello', name)

player = int(input(name + ' choose your option: (1)Stone (2)Paper (3)Scissors: '))


if player == 1:
    play = "Stone"
if player == 2:
    play = "Paper"
if player == 3:
    play = "Scissors"

if pc == 1:
    computer = "Stone"
if pc == 2:
    computer = "Paper"
if pc == 3:
    computer = "Scissors"


print(name + ' chooses: ', play)
print('PC chooses: ', computer)


if player == 1 and pc == 1:
    print("Tie")
elif player == 1 and pc == 2:
    print("You loose")
elif player == 1 and pc == 3:
    print("You wins")
elif player == 2 and pc == 1:
    print("you wins")
elif player == 2 and pc == 2:
    print("Tie")
elif player == 2 and pc == 3:
    print("You loose")
elif player == 3 and pc == 1:
    print("You loose")
elif player == 3 and pc == 2:
    print("You wins")
elif player == 3 and pc == 3:
    print("Tie")
else:
    print("Invalid option")

   
 