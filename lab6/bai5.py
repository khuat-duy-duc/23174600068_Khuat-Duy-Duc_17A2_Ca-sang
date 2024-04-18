#Nhập dãy số
day_so=[] 
while True:
    a = int(input("Nhập vào phần tử của dãy (0 để dừng lại): "))
    if a != 0:
        day_so.append(a)
    else:
        break
print(day_so)
#kiểm tra cấp số cộng
if len(day_so)<2:
    print("Dãy số quá ngắn")
else:
    congsai=day_so[1]-day_so[0]
    check=True
    for i in range(1,len(day_so)):
        if day_so[i]-day_so[i-1]!=congsai:
            check=False
            break
    if check==True:
        print("Dãy số tạo thành cấp số cộng")
    else:
        print("Dãy số không tạo thành cấp số cộng")


