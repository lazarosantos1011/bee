par = []
impar = []
cont = 0
p = 0
i = 0

while cont < 15:
    X = int(input())
    if X % 2 == 0:
        par.append(X)
        p = p + 1
    if X % 2 != 0:
        impar.append(X)
        i = i + 1
    
    if p > 4:
        for c in range(0,5):
            print(f"par[{c}] = {par[c]}")
        par = []
        p = 0
    if i > 4:
        for c in range(0,5):
            print(f"impar[{c}] = {impar[c]}")
        impar = []
        i = 0
    
    cont = cont + 1

if p > 0:
    for h in range(p):
        print(f'par[{h}] = {par[h]}')    
if i > 0:
    for j in range(i):
        print(f'impar[{j}] = {impar[j]}')
