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
        super().__init__(nome, ano)
        self.duracao = duracao


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas


vingadores = Filme("Vingadores - End game", 2019, 90)
friends = Serie("Friends", 1995, 5)

vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
friends.dar_likes()

playlist = [vingadores, friends]
for i in playlist:
    print(f'Nome: {i.nome} - Likes: {i.likes}')
