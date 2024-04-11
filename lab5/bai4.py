chuoi=input("nhập chuỗi số vô : ")
chuoiso=""
for i in chuoi:
    if i>='0' and i<='9':
        chuoiso+=i
if chuoiso.isdigit():
    n= int(chuoiso)
    if n>1:
        for i in range(2,n):
            if (n%i)==0:
                print(f"{n} không phải là số nguyên tố")
                break
        else:
            print(f"{n} là số nguyên tố ")