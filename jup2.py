'''#1
aux = []
tamanho = 5
for x in range(tamanho):
    d = int(input())
    aux.append(d)
print(aux)
'''
#2
aux = []
tamanho = 10
for x in range(tamanho):
    d = int(input())
    aux.append(d)
aux = reversed(aux)
print(*aux)