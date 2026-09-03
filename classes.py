class Cachorro:
    #Método Constructor
    def __init__(self, nome, raca, tamanho, cor_pelo): #Atributos da classe
        self.nome = nome
        self.raca = raca
        self.tamanho = tamanho
        self.cor_pelo = cor_pelo


zeca = Cachorro("Zeca", "Viralata", "Médio", "Caramelo")
brutus = Cachorro("Brutus", "Pitbull", "Grande", "Preto")
mel = Cachorro("Mel", "Yorkshire", "Pequeno", "Marrom")

print(zeca.nome)
