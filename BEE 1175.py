N=[]
for i in range(20):
    Y=int(input())
    N.append(Y)
a=N[::-1]
for j in range(20):
    print('N[{}] = {}'.format(j,a[j]))
