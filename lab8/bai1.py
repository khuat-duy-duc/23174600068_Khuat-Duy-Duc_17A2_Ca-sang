def nguyen_to(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
print("Các số nguyên tố nhỏ hơn 1000 :")
for i in range(1000):
    if nguyen_to(i):
        print(i,end=",")
def couple():
    chuoi= []
    for i in range(2, 1000):
        if nguyen_to(i) and nguyen_to(i + 2):
            chuoi.append((i,i+ 2))
    return chuoi

list_chuoi_doi=couple()
print("\n Các chuỗi nguyên tố đôi nhỏ hơn 1000 :")
for couple in list_chuoi_doi:
    print(couple[0],couple[1],end=",")
