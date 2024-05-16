def cubesum(n):
    tong= 0
    while n != 0:
        du= n % 10
        tong+= du** 3
        n //= 10
    return tong
print("Tổng của các lập phương của các chữ số riêng lẻ của là:", cubesum(123))

def PrintArmstrong():
    for i in range(1, 1000):
        if i== cubesum(i):
            print(i, end=" ")
print("Các số Armstrong dưới 1000 là:")
PrintArmstrong()

def isArmstrong(n):
    return n == cubesum(n)
    
n=1231123
print(f"\n {n} có phải là số Armstrong không?", isArmstrong(n))




    