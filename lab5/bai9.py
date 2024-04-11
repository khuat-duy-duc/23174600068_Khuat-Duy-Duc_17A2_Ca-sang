chuoicu = input("Nhập chuỗi vô :")
chuoimoi = input("Nhập chuỗi mới :")
duoc=0
if len(chuoicu) != len(chuoimoi):
    duoc+=1
else:
    for i in range(len(chuoicu)):
        if chuoicu[i]!=chuoimoi[i]:
            duoc+=1
            break
if duoc:
    print("Có thể thay đổi chuỗi nhé")
else:
    print("Không thể thay đổi được nhé")