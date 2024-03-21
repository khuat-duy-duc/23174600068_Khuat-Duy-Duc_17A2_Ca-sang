a1,b1=map(int,input("Nhập hệ số góc và hệ số tự do của đường thẳng 1 : ").split())
a2,b2=map(int,input("Nhập hệ số góc và hệ số tự do của đường thẳng 2 : ").split())
if a1==a2 and b1!=b2:
    print("Đường thẳng 1 song song với đường thẳng 2")
elif a1!=a2:
    print("Đường thẳng 1 cắt đường thẳng 2")
elif a1*a2==(-1):
    print("Đường thằng 1 vuông góc với đường thẳng hai")