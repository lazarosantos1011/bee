T = int(input())
N = []
j = 0
i = 0
while i < (1000):
    N.append(j)
    print(F"N[{i}] = {j}")
    
    if j < (T - 1):
        j = j + 1
    else:
        j == T - 1
        j = 0
    i = i + 1
