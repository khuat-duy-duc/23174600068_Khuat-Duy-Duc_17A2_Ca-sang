banana=""
n=int(input("Nhập số nguyên vào : "))
if n<=0:
    print("phải là số nguyên dương")
else:
    while n>0:
        a=n%2
        banana=str(a)+banana
        n=n//2
    print("Số nhị phân sau khi chuyển đổi là ",banana)