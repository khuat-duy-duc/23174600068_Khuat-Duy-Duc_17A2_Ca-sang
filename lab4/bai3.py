n = int(input("Nhập số từ bàn phím: "))
count = 1
while True: 
    n = n//10  
    if n == 0:
        break
    count += 1
print(count)