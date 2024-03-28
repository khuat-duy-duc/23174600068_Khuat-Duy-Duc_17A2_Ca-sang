# a
n=int(input("Nhập n vô : "))
if n<=0:
    print("Nhập lại n ")
else:
    sum=0
    for i in range(1,n+1):
        sum+=i
    print(sum)
# b
if n<=0:
    print("Nhập lại n đi")
else:
    cho=0
    for i in range(1,n+1):
        cho=cho+1/i
    print(cho)
#c
import math
if n<=0:
    print("Mời nhập lại n!")
else:
    sau=0
    for i in range(1,n+1):
        sau=sau+1/math.sqrt(2*i)
    print(sau)
#d
if n<=0:
    print("Mời nhập lại n!")
else:
    duc=0
    for i in range(1,n+1):
        duc=duc+(-1)**(i+1)/i
    print(duc)