chuoi = input("Nhập chuỗi văn bản: ")
chontim= input("Nhập từ cần tìm kiếm: ")
chocopie = chuoi.find(chontim)
print("Từ được tìm thấy tại vị trí:",chocopie)
xh=chuoi.count(chontim)
xhnhieu=""
xhnhieunhat=0
for i in chuoi.split():
    if i==chontim:
        solan_xh=chuoi.count(i)
        if solan_xh>xhnhieunhat:
            solan_xh=xhnhieunhat
            xhnhieu=i
print("Số lần xuất hiện là : ",xh)
print("Từ xuất hiện nhiều nhất là : ",xhnhieu)