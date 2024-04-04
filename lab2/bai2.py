n=int(input("Nhập vào số nguyên : "))
deptrai=n//1000
duc=deptrai%10
if duc==0:
    print("0")
else:
    print(f"Chữ số hàng nghìn là : {duc}")