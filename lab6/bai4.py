#số fibonacci
n= int(input("Nhập số lượng số Fibonacci cần tạo: "))
day_fibo = [0, 1] if n >= 2 else [0] if n == 1 else []
for i in range(2, n):
    day_fibo.append(day_fibo[-1] + day_fibo[-2])
print(f"Danh sách Fibonacci gồm {n} số đầu tiên là:",day_fibo)
#số nguyên tố
n = 100
day_snt=[num for num in range(2, n+1) if all(num % i != 0 for i in range(2, int(num**0.5) + 1) )]
print(day_snt)

