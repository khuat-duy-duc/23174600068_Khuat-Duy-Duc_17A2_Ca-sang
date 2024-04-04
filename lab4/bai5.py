while True:
    a,b=map(int,input("Nhập số vô : ").split())

    print(f"{a} + {b} = {a+b}")
    print(f"{a} - {b} = {a-b}")
    print(f"{a} * {b} = {a*b}")
    print(f"{a} / {b} = {a/b}")
    n=input("Bạn có muốn tiếp tục không (0 để dừng lại ) : ")
    if n=='0':
        break