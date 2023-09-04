class Programa:

  def __init__(self, nome, ano):
    self._nome = nome.title()
    self.ano = ano
    self._likes = 0

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

  def __str__(self):
    return f'{self._nome} - {self.ano} - {self._likes} Likes'

  def imprime(self):
    print(f'{self._nome} - {self.ano} - {self._likes} Likes')


class Filme(Programa):

  def __init__(self, nome, ano, duracao):
    super().__init__(nome, ano)
    self.duracao = duracao

  def __str__(self):
    return f'Nome: {self.nome} - {self.duracao} min - Likes: {self.likes}'


class Serie(Programa):

  def __init__(self, nome, ano, temporadas):
    super().__init__(nome, ano)
    self.temporadas = temporadas

  def __str__(self):
    return f'Nome: {self.nome} - {self.temporadas} temporadas - Likes: {self.likes}'


class Playlist(list):

  def __init__(self, nome, programas):
    self.nome = nome
    self._programas = programas

  def __getitem__ (self, item):
    self._programas[item]

  @property
  def listagem(self):
    return self._programas 


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('Todo mundo em pânico', 199, 100)
demolidor = Serie('Demolidor', 2016, 2)

vingadores.dar_likes()
tmep.dar_likes()

atlanta.dar_likes()
demolidor.dar_likes()

filmes_series = [vingadores, atlanta, demolidor, tmep]
fim_de_semana = Playlist('Fim de Semana', filmes_series)


for programa in fim_de_semana.listagem:
  print(programa)
