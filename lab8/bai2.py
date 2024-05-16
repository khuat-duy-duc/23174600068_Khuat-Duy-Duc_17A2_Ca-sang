def giai_thua(n):
    if n== 0 or n== 1:
        return 1
    result=1
    for i in range(2,n+ 1):
        result *= i
    return result

def hoan_vi(n, r):
    return giai_thua(n)/giai_thua(n - r)

def to_hop(n, r):
    return hoan_vi(n, r)/giai_thua(r)

n= int(input("Nhập n: "))
r = int(input("Nhập r: "))

if n < r:
    print("Số phần tử lấy không thể lớn hơn số phần tử.")
else:
    print("Hoán vị là:",hoan_vi(n, r))
    print("Tổ hợp là:",to_hop(n, r))