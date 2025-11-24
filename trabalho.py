# Integrantes: Éverson e Victor Andrei

class TabelaHash:
    def __init__(self, tamanho=10):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]

    def funcao_hash(self, nome: str) -> int:
        total = 0
        for indice, caractere in enumerate(nome, start=1):
            total += ord(caractere) * indice
        return total % self.tamanho

    def inserir(self, nome: str):
        indice = self.funcao_hash(nome)
        self.tabela[indice].append(nome)

    def mostrar_distribuicao(self):
        print("\n=== Distribuição na Tabela Hash ===")
        for indice, slot_lista in enumerate(self.tabela):
            print(f"{indice:2} | {slot_lista}")

    def contar_colisoes(self):
        colisoes = 0
        for slot_lista in self.tabela:
            if len(slot_lista) > 1:
                colisoes += len(slot_lista) - 1
        return colisoes
    
nomes = [
    "João", "João Silva", "Ana Clara", "Ana Cláudia",
    "Andressa", "André", "Roberta", "Roberto",
    "Carla", "Karl", "Marcos", "Marcus",
    "Pablo", "Pabllo", "Tiago", "Ronaldo",
    "Kelvin", "Benjamin", "Éverson", "Victor Andrei"
]

tabela = TabelaHash(tamanho=10)

for nome in nomes:
    tabela.inserir(nome)

tabela.mostrar_distribuicao()

print("\nTotal de colisões:", tabela.contar_colisoes())