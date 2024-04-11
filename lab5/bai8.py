str=input("Nhập chuỗi vào : ")
if len(str)<=10:
    print("Chuỗi so short")
else:
    a=str[1:8]
    print("phần a bằng : ",a)

    b=str[4:9]
    print("phần b bằng : ",b)

    c=str[-3:]
    print("phần c bằng : ",c)

    d=str.lower()
    print("phần d bằng : ",d)

    e=str.upper()
    print("phần e bằng : ",e)

    f=str[::-1]
    print("phần f bằng : ",f)