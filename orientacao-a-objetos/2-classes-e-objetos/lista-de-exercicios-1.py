# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.
# Crie uma instância da classe carro.
# Faça o carro "andar" utilizando os métodos da sua classe.
# Faça o carro "parar" utilizando os métodos da sua classe.

class Carro:
    def __init__(self, cor, modelo):
        self.ligado = False
        self.cor = cor
        self.modelo = modelo
        self.velocidade = 0

    def liga(self):
        self.ligado = True
        print(f"O {self.modelo} {self.cor} está ligado.")

    def desliga(self):
        self.ligado = False
        self.velocidade = 0
        print(f"O {self.modelo} {self.cor} está desligado.")

    def acelera(self, valor):
        if self.ligado:
            self.velocidade += valor
            print(f"O carro está acelerando, velocidade atual: {self.velocidade} km/h.")
        else:
            print("O carro precisa estar ligado para acelerar.")

    def desacelera(self, valor):
        if self.ligado:
            self.velocidade -= valor
            if self.velocidade < 0:
                self.velocidade = 0
            print(f"O carro está desacelerando, velocidade atual: {self.velocidade} km/h.")
        else:
            print("O carro precisa estar ligado para desacelerar.")

#Instância da classe carro
meu_carro = Carro("Vermelho", "Gol")

#Faça o carro "andar"

meu_carro.liga()

meu_carro.acelera(20)
meu_carro.acelera(30)

# Faça o carro "parar"
meu_carro.desacelera(50)
meu_carro.desliga()
meu_carro.desliga()
