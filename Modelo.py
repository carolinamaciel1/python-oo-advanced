class Programa:
    def __init__(self, nome, ano):
        self._nome = nome
        self._ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        self._nome = nome
        self.ano = ano
        self.duracao = duracao
        self._likes = 0


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        self._nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self._likes = 0


vingadores = Filme("Vingadores - End game", 2019, 90)
friends = Serie("Friends", 1995, 5)

# print(vingadores._Filme__nome)
print(vingadores.nome)
print(f'Nome: {friends.nome} - Ano: {friends.ano}')
