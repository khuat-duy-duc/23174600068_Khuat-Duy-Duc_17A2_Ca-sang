mang=[]
n=int(input("Số phần tử nhập vào mảng : "))
for i in range(n):
    a=int(input("Nhập phần tử vào : "))
    mang.append(a)
print(mang)

pool=[]
for i in mang:
    check=True
    if i>1:
        for j in range(2,i):
            if i%j==0:
                check=False
        if check==True:
            pool.append(i)
print("Các số nguyên tố trong mảng là : ",pool)


bang=[]
for i in mang:
    sum=0
    for j in range(1,i):
        if i%j==0:
           sum+=j
    if sum==i:
        bang.append(i)
print(bang)