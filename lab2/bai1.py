a,b=map(int,input("nhập các hệ số : ").split())
if a==0:
    if b!=0:
        print("phường trình vô nghiệm")
    else:
        print("phương trình vô số nghiệm")
else:
    x=-b/a
    print(f"Phương trình có nghiệm duy nhất x = {x}")