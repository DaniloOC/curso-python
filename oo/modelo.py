from abc import ABCMeta, abstractmethod # usando abstract base method ABC's

class Programa(metaclass = ABCMeta):
    def __init__(self, nome, ano):
        self.__nome = nome.title()
        self.ano = ano
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1

    @abstractmethod
    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.likes} Likes'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.duracao} min. - {self.likes} Likes'
        # return super().__str__()

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.temporadas} Temporadas - {self.likes} Likes'

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self.__programas = programas

    def __getitem__(self, item):
        return self.__programas[item]

    @property
    def listagem(self):
        return self.__programas

    def __len__(self):
        return len(self.__programas)

vingadores = Filme('Vingadores - Guerra Infinita', 2019, 160)
atlanta = Serie('Atlanta', 2018, 3)
tmep = Filme('Todo mundo em pânico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)

vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist('Fim de semana', filmes_e_series)

print(f'Tamanho do playlist: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana:
    print(programa)
    print(repr(programa))

print(f'Tá ou não tá? {demolidor in playlist_fim_de_semana}')