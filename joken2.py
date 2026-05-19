import random

op = ["pedra", "papel", "tesoura"]

while True :
    pc = random.choice(op)

    jog = input("Pedra, papel ou tesoura? ").lower()

    if jog == "sair":
        print("Saindo...")
        break

    elif jog not in op :
        print("Opção inválida")

    else:
        print(f"Computador escolheu {pc}")

        if jog == pc:
            print("Empate")

        elif jog == "pedra" and pc == "tesoura":
            print("Você venceu")

        elif jog == "tesoura" and pc == "papel":
            print("Você venceu")

        elif jog == "papel" and pc == "pedra":
            print("Você venceu")

        else:
            print("Computador venceu")