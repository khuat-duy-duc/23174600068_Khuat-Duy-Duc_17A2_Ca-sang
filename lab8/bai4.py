def sumPdivisors(n):
    tong_Pd = 0
    for i in range(1,n):
        if n % i == 0:
            tong_Pd+=i
    return tong_Pd
print("Tổng các ước số chính của là:", sumPdivisors(220))

