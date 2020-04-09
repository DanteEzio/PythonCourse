#Realizar un programa que pueda jugar el juego piedra papel o tijera
#Pedirle al jugador que eija su opcion
#Hacer que la computadora eliga una accion

from random import randint

pc = randint(1,3)

print("Welcome!")
name = input("Choose your player name: ")
print("Hello ", name)
player = int(input("Input your option: (1)Stone, (2)Paper, (3)Scissors: " ))

if player == 1:
    print("You selected stone")
elif player == 2:
    print("You selected paper")
elif player == 3:
    print("You selected Scissor")
#else:
#    print("Input a valid option")

if pc == 1:
    print("PC selected stone")
elif pc == 2:
    print("PC selected paper")
elif pc == 3:
    print("PC slected scissor")
#else:
#    print("Input a valid option")



if player == 1 and pc == 1:
    print("Tie")
elif player == 2 and pc == 2:
    print("Tie")
elif player == 3 and pc == 3:
    print("Tie")
elif player == 1 and pc == 2:
    print("You loose")
elif player == 1 and pc == 3:
    print("You win")
elif player == 2 and pc == 1:
    print("You win")
elif player == 2 and pc == 3:
    print("You loose")
elif player == 3 and pc == 1:
    print("You loose")
elif player == 3 and pc == 2:
    print("You win")
else:
    print("You selected", player, "a invalid option")

