def sumPdivisors(n):
    tong_Pd = 0
    for i in range(1,n):
        if n % i == 0:
            tong_Pd+=i
    return tong_Pd

def amicable(n,m):
    return sumPdivisors(n) ==m and sumPdivisors(m) ==n

n= 220
m= 284
if amicable(n,m):
    print(n, "và",m, "là một cặp số amicable.")
else:
    print(n, "và",m, "không phải là một cặp số amicable.")