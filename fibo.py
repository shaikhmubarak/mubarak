def fibo(n):
    fibTable = [0,1]
    for i in range(2,n+1):
        fibTable.append(fibTable[i-1] + fibTable[i-2])
    return fibTable[n]
print(fibo(10))
