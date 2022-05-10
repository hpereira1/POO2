'''
class Conta:
  def __init__(self, nome, saldo):
    self.nonme = list(nome)
    self.saldo = saldo

  def deposito(self, valor):
    self.saldo = float(self.saldo) + float(valor)
    print(f"Seu Saldo é de:{self.saldo}\n")

  def saque(self, valor):
    if float(self.saldo) >= float(valor):
      self.saldo = float(self.saldo) - valor
      print(f"Seu Saldo é de:{self.saldo}\n")
    else:
      print("Saldo Insuficiente")

  def versaldo(self, saldo):
    print(f"Seu Saldo é de:{self.saldo}\n")

class Premium(Conta):
  def __init__(self, nome, saldo, limiteespecial):
    Conta.__init(self, nome, saldo)
    self.limiteespecial = limiteespecial
  
  def limiteespecial(self, saldo, limiteespecial):
    if saldo == 0:
      limiteespecial = self.saldo + 1000
'''
'''
dictbooks = {}
class Funcionario:
  def __init__(self, nome):
    self.nome = nome
  
  def preencher(self):
    titulo = input()
    autor = input()
    ano = input()
    editora = input()
    edicao = input()
    volume = input()
    book = books(autor, ano, editora, edicao, volume)
    dictbooks.update({titulo: books})

class books:
  def __init__(self, titulo, autor, ano, editora, edicao, volume):
    self.titulo = titulo
    self.autor = autor
    self.ano = ano
    self.editora = editora
    self.edicao = edicao
    self.volume = volume
  
  def pesquisa(self):
    aux = input("digite o titulo para pesquisa: ")
    while aux not in dictbooks.keys():
      aux = input("digite um titulo valido para pesquisa: ")
    print(dictbooks[aux])
'''
'''class Carta:
    def __init__(self, naipe, posit):
        self.naipe = naipe
        self.posit = posit
    naipe = ("paus", "ouro", "copas", "espadas")
    posit = ('as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'rainha', 'valete', 'rei')
 

class Baralho:
   def __init__(self):
        self.cartas = []
        for naipe in range(4):
            for  posit in range(1, 14):
                carta = Carta(naipe, posit)
                self.cartas.append(carta)'''
'''
class Televisao:
    def __init__(self, tamanho, marca):
        self.status = False
        self.canal = 2
        self.tamanho = tamanho
        self.marca = marca
    
    def muda_canal_pra_cima(self):
        if self.canal == 99:
            self.canal = 1
        self.canal = self.canal + 1
        print(self.canal)

    def muda_canal_pra_baixo(self):
        if self.canal == 1:
            self.canal == 99
        self.canal = self.canal - 1
        print(self.canal)'''
dictestados = {}
dictcidades = {}
class Estado:
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
        self.cidades = []
        
    def criarestado(self):
        nome = input()
        sigla = input()
        estado = Estado(sigla)
        dictestados.update({nome: estado})


class Cidade:
    def __init__(self, nome, populacao):
        self.nome = nome
        self.populacao = populacao
    
