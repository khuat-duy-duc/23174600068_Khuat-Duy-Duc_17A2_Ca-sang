snack=[]
n=int(input("Số phần tử trong bim bim : "))
for i in range(n):
    a=float(input("Nhập phần tử : "))
    snack.append(a)
print(snack)

max=0
for i in range(len(snack)):
    if max<snack[i]:
        max=snack[i]
print("Phần tử lớn nhất trong bim bim là ",max)


print("Phần tử nhỏ nhất trong bim bim là : ",min(snack))