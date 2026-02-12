nivel = int(input("Digite o seu nível: "))
if nivel >= 10:import time

# 1) Nível do Jogador
nivel = int(input("Digite o seu nível: "))
if nivel >= 10:
    print("Modo ranqueado está liberado!")
else:
    print("Modo ranqueado ainda está bloqueado.")

print("-" * 20)

# 2) Vida do Personagem
vida = int(input("Digite a vida do personagem (0-100): "))
if vida <= 0:
    print("Game Over.")
else:
    print("O personagem está vivo.")

print("-" * 20)

# 3) Valor do Dano
dano = int(input("Digite o valor do dano: "))
if dano % 2 == 0:
    print("Ataque crítico.")
else:
    print("Ataque normal.")

print("-" * 20)

# 4) Fases do Jogo
fases = int(input("Quantas fases o jogo tem? "))
for i in range(1, fases + 1):
    print(f"Iniciando fase {i}...")

print("-" * 20)

# 5) Energia do Jogador
energia = int(input("Digite a energia do jogador (0-100): "))
if energia >= 70:
    print("Energia: Alta")
elif 30 <= energia < 70:
    print("Energia: Média")
else:
    print("Energia: Baixa")

print("-" * 20)

# 6) Contagem para Partida
print("Iniciando em:")
contador = 3
while contador > 0:
    print(contador)
    time.sleep(1) # Pausa de 1 segundo
    contador -= 1
print("Partida iniciada!")

print("-" * 20)

# 7) Pontuação e Seleção de Personagem
pontuacao = int(input("Digite a pontuação do jogador: "))
if pontuacao >= 1000:
    print("Progresso salvo!")
else:
    print("Progresso não atingiu o mínimo para salvar.")

print("\nEscolha seu personagem:")
print("1 - Guerreiro")
print("2 - Mago")
print("3 - Arqueiro")

opcao = input("Opção: ")

if opcao == "1":
    print("Você escolheu: Guerreiro")
elif opcao == "2":
    print("Você escolheu: Mago")
elif opcao == "3":
    print("Você escolheu: Arqueiro")
else:
    print("Opção inválida.")
