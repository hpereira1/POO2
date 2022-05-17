'''#1
aux = []
tamanho = 5
for x in range(tamanho):
    d = int(input())
    aux.append(d)
print(aux)
'''
'''#2
aux = []
tamanho = 10
for x in range(tamanho):
    d = int(input())
    aux.append(d)
aux = reversed(aux)
print(*aux)'''
'''#3
a = float(input())
b = float(input())
c = float(input())
d = float(input())
media = (a + b + c +d)/4
print(f'as notas são {a}, {b}, {c} e {d}. A média é {media}')
'''
'''#4
aux = 0
letras = []
consoantes = [] 
for i in range(10):
    letra = input().upper()
    if letra not in 'AEIOU':
        consoantes.append(letra)
        aux += 1
print(f'{aux} consoantes, {consoantes}')
'''
'''#5
numeros = []
par = []
impar = []
for x in range(20):
    aux = int(input())
    numeros.append(aux)
    if aux%2 ==0:
        par.append(aux)
    else:
        impar.append(aux)
print(f'{par} pares, {impar} impar e {numeros}')'''
'''
#6
listamedias = []
cont = 0
for i in range(10):
    soma = 0
    for j in range(4):
        aux = float(input(f'nota {j+1}: '))
        soma +=aux
    media = (soma)/4
    listamedias.append(media)
print(listamedias)
'''
'''#7
numeros = []
produto = 1
soma = 0
for i in range(5):
    aux = float(input())
    numeros.append(aux)
for  x in numeros:
    produto =produto * x
    soma = soma + x
print(f'soma = {soma}. produto = {produto}, lista = {numeros}')'''

#8
pessoas = []
for x in range(5):
    aux = []
    idade = int(input())
    altura = float(input())
    pessoas.append(altura, idade)
    aux.clear()
print(pessoas)