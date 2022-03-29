T = int(input())
for i in range(T):
    X = int(input())
    f = [0,1]
    
    if X > 1:
        for j in range(2, X+1):
            
            f.append(f[j-2] + f[j-1])
        print(f"Fib({X}) = {f[X]}")
    if X <= 1:
        print(f"Fib({X}) = {f[X]}")
    