#a
n=int(input("Nhập chiều cao n vào : "))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("* ",end="")
    print()
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for j in range(n-i):
        print("* ",end="")
    print()
#b
n=int(input("Nhập chiều cao của tam giác vào : "))
a=int(input("nhập số hàng hình chữ nhật : "))
b=int(input("nhập số cột hình chữ nhật : "))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(2*i+1):
        print("*",end="")
    print()
for i in range(1,a+1):
    for j in range(a+2):
        print(" ",end="")
    for j in range(1,b+1):
        print("*",end="")
    print()