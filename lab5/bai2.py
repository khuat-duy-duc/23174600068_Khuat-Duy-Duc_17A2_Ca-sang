str1 = input("Nhập chuỗi ký tự thứ nhất: ")
str2 = input("Nhập chuỗi ký tự thứ hai: ")
chuoi_chung_ngan_nhat = ""
do_dai_ngan_nhat = float('inf')
for i in range(len(str1)):
    for j in range(len(str2)):
        k = 0
        while (i + k < len(str1) and j + k < len(str2) and str1[i + k] == str2[j + k]):
            k += 1
        if k > 0 and k < do_dai_ngan_nhat:
            chuoi_chung_ngan_nhat = str1[i:i + k]
            do_dai_ngan_nhat = k
print("Chuỗi ký tự con chung ngắn nhất là:", chuoi_chung_ngan_nhat)