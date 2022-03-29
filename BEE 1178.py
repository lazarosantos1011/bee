X = float(input())
N = []
X = X * 2
for i in range(100):
    N.append(X)
    N[0] = X
    print(F"N[{i}] = {X / 2:.4f}")
    X = X / 2
