import random
import os
from collections import deque

# Função para criar o baralho de cartas
def criar_baralho():
    naipes = ['♥', '♦', '♣', '♠']
    valores = [str(numero) for numero in range(1, 14)]
    baralho = [f"{valor}{naipe}" for valor in valores for naipe in naipes]
    random.shuffle(baralho)
    return baralho

# Função para verificar se um grupo de três cartas forma uma trinca
def verificar_trinca(cartas):
    if len(cartas) != 3:
        return False

    valores = [carta[:-1] for carta in cartas]
    naipes = [carta[-1] for carta in cartas]

    # Trinca de valores iguais com naipes diferentes
    if len(set(valores)) == 1 and len(set(naipes)) == 3:
        return True

    # Trinca de sequência numérica com o mesmo naipe
    valores_numericos = sorted(map(int, valores))
    if valores_numericos[2] - valores_numericos[0] == 2 and len(set(naipes)) == 1:
        return True

    return False

# Função para organizar as cartas da mão em trincas válidas
def organizar_mao(cartas_na_mao):
    trincas = []
    cartas_restantes = cartas_na_mao[:]

    # Procurar trincas de valores iguais com naipes diferentes
    for valor in set(carta[:-1] for carta in cartas_restantes):
        cartas_com_valor = [carta for carta in cartas_restantes if carta[:-1] == valor]
        if len(cartas_com_valor) >= 3:
            trincas.append(cartas_com_valor[:3])
            for carta in cartas_com_valor[:3]:
                cartas_restantes.remove(carta)

    # Procurar trincas de sequência numérica com o mesmo naipe
    for naipe in set(carta[-1] for carta in cartas_restantes):
        cartas_do_naipe = sorted([carta for carta in cartas_restantes if carta[-1] == naipe], key=lambda x: int(x[:-1]))
        for i in range(len(cartas_do_naipe) - 2):
            possivel_sequencia = cartas_do_naipe[i:i + 3]
            valores_sequencia = sorted(map(int, [carta[:-1] for carta in possivel_sequencia]))
            if valores_sequencia[2] - valores_sequencia[0] == 2:
                trincas.append(possivel_sequencia)
                for carta in possivel_sequencia:
                    cartas_restantes.remove(carta)

    return trincas, cartas_restantes

# Classe principal do jogo de cartas
class JogoDeCartas:
    def __init__(self):
        self.baralho = criar_baralho()
        self.pilha_descarte = []
        self.jogadores = []
        self.fila_turnos = deque()

    # Adicionar um jogador ao jogo
    def adicionar_jogador(self, nome):
        cartas_iniciais = [self.baralho.pop() for _ in range(6)]
        self.jogadores.append({"nome": nome, "mao": cartas_iniciais, "trincas": []})
        self.fila_turnos.append(nome)
        print(f"{nome} entrou no jogo com as cartas: {cartas_iniciais}")

    # Executar o turno de um jogador
    def executar_turno(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        if not self.fila_turnos:
            print("Nenhum jogador disponível!")
            return

        nome_jogador = self.fila_turnos.popleft()
        jogador = next(jogador for jogador in self.jogadores if jogador["nome"] == nome_jogador)

        print(f"\nTurno de {jogador['nome']}. Mão: {jogador['mao']}")
        print(f"Carta no topo do descarte: {self.pilha_descarte[-1] if self.pilha_descarte else 'Nenhuma'}")

        # Escolher entre comprar do baralho ou pegar do descarte
        print("Escolha: [1] Comprar do baralho, [2] Pegar do descarte")
        escolha = input()

        if escolha == "1":
            nova_carta = self.baralho.pop()
            print(f"{jogador['nome']} comprou {nova_carta} do baralho.")
        elif escolha == "2" and self.pilha_descarte:
            nova_carta = self.pilha_descarte.pop()
            print(f"{jogador['nome']} pegou {nova_carta} do descarte.")
        else:
            print("Escolha inválida! Pulando turno.")
            self.fila_turnos.append(nome_jogador)
            return

        jogador["mao"].append(nova_carta)

        # Jogador descarta uma carta
        print("Escolha uma carta para descartar:")
        for indice, carta in enumerate(jogador["mao"], start=1):
            print(f"{indice}. {carta}")
        try:
            indice_descarte = int(input()) - 1
            carta_descartada = jogador["mao"].pop(indice_descarte)
            self.pilha_descarte.append(carta_descartada)
            print(f"{jogador['nome']} descartou {carta_descartada}.")
        except (ValueError, IndexError):
            print("Descarte inválido! Carta devolvida à mão.")
            jogador["mao"].remove(nova_carta)

        # Organizar cartas em trincas
        jogador["trincas"], jogador["mao"] = organizar_mao(jogador["mao"])
        print(f"Trincas de {jogador['nome']}: {jogador['trincas']}")
        print(f"Cartas restantes na mão: {jogador['mao']}")

        # Verificar vitória
        if len(jogador["mao"]) == 0:
            print(f"{jogador['nome']} venceu o jogo ao ficar sem cartas!")
            exit()

        # Recolocar o jogador na fila de turnos
        self.fila_turnos.append(nome_jogador)

    # Mostrar o estado atual do jogo
    def exibir_estado_jogo(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nEstado do jogo:")
        for jogador in self.jogadores:
            print(f"{jogador['nome']} - Mão: {jogador['mao']} - Trincas: {jogador['trincas']}")
        print("Cartas no descarte:", self.pilha_descarte[-5:])

# Inicializar e executar o jogo
jogo = JogoDeCartas()
jogo.adicionar_jogador("Jogador 1")
jogo.adicionar_jogador("Jogador 2")

while True:
    jogo.executar_turno()
    jogo.exibir_estado_jogo()
