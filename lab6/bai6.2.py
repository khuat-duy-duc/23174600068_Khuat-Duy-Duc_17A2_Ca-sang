#tạo ma trận vuộng
n=int(input("Kích thước của mà trận vuông là : "))
matrix=[]
for i in range(n):
    row=[]
    for j in range(n):
        phantu=int(input(f"Nhập các phần tử hàng {i} cột {j} : "))
        row.append(phantu)
    matrix.append(row)
print(matrix)
#tìm ma trận nghịch đảo
