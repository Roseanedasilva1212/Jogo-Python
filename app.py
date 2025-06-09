import random

def adivinhe_o_numero():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print("🎮 Bem-vindo ao Jogo: Adivinhe o Número!")
    print("Eu escolhi um número entre 1 e 100. Tente adivinhar!")

    while True:
        try:
            chute = int(input("Digite seu palpite: "))
            tentativas += 1

            if chute < numero_secreto:
                print("🔼 O número é maior! Tente novamente.")
            elif chute > numero_secreto:
                print("🔽 O número é menor! Tente novamente.")
            else:
                print(f"🎉 Parabéns! Você acertou em {tentativas} tentativas.")
                break
        except ValueError:
            print("⚠️ Por favor, digite um número válido!")

adivinhe_o_numero()
