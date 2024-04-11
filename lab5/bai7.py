banana= input("Nhập chuỗi: ")
con= 0
cat = 0
yeu = 0
chicken= 0
for i in banana:
    if i.islower():
        con+= 1
    elif i.isupper():
        cat+= 1
    elif i.isdigit():
        yeu += 1
    else:
        chicken+= 1
print("Số chữ thường trong chuỗi:",con)
print("Số chữ hoa trong chuỗi:",cat)
print("Số chữ số trong chuỗi:",yeu)
print("Số ký tự đặc biệt trong chuỗi:",chicken)
