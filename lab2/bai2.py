n=int(input("Nhập vào số nguyên : "))
deptrai=n//1000
if deptrai==0:
    print("0")
else:
    print(f"Chữ số hàng nghìn là : {deptrai}")