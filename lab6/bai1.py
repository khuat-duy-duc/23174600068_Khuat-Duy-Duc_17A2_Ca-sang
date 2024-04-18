#1
danhsach=[]
n=int(input("Số phần tử nguyên dương nhập từ bàn phìm là : "))
for i in range(n):
    a=int(input("Nhập phần tử vào : "))
    if a>0:
       danhsach.append(a)
print(danhsach)
#2
sum=0
tong=0
for i in danhsach:
    if i%2==0:
        sum+=i
    if i%2!=0:
        tong+=i
print("Tổng các số chẵn trong danh sách là",sum)
print("Tổng các số lẻ trong danh sách là ",tong)
