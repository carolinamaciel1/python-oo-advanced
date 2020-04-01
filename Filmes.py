class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome
        self.__ano = ano
        self.duracao = duracao

    @property
    def nome(self):
        return self.__nome


class Serie:
    def __init__(self, nome, ano, likes):
        self.__nome = nome.title()
        self.ano = ano
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def dar_likes(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome


vingadores = Filme("Vingadores - End game", 2019, 90)
friends = Serie("Friends", 1995, 5)

#print(vingadores._Filme__nome)
print(vingadores.nome)
print(f'Nome: {friends.nome} - Ano: {friends.ano}')
