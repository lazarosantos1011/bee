N = int(input())
X = input()
X = X.split()

for i in range(len(X)):
    X[i] = int(X[i])

menorValor = X[0]
posicao = 0
for j in range(1,len(X)):
    if X[j] < menorValor:
        menorValor = X[j]
        posicao = j

print('Menor valor: {}'.format(menorValor))
print('Posicao: {}'.format(posicao))
