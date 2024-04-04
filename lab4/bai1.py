#a
tong=0
so=0
while tong<=1000:
    n=int(input("Nhập n vào : "))
    so=so+1
    if n%2!=0:
        tong+=n
    print(tong)
#b
sum=0
sa=0
while sum<=1000:
    n=int(input("Nhập số nguyên vô : "))
    sa=sa+1
    if n%2==0:
        sum+=n
    print(sum)
#c
print(f"Số lượng số nguyên đa nhập là : {sa+so}")