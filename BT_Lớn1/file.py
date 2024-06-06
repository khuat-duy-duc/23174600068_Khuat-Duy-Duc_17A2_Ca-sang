import random
import csv

def tung_xucsac():
    return random.randint(1, 6)

def choi(diem):
    tong= 0
    tungs = 0

    while True:
        tungs+= 1
        tung=tung_xucsac()
        tong+=tung
        print(f"Lần { tungs} ,tung được { tung}. Tổng điểm: { tong}")

        if tong>=diem:
            break

        n= input("Bạn có muốn tung tiếp không? (yes/no): ").lower()
        if n!= 'yes':
            break

    if tong >=diem:
        print(f"You win!")
        result = "Win"
    else:
        print(f"You lose.")
        result = "Lose"

    ti_le= (6 - diem+ 1) / 6

    return tong, result,ti_le

def save_to_csv(data):
    with open('file.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)



diem= int(input("Nhập số điểm mong muốn : "))
tong = int(input("Nhập số lần chơi : "))
for game in range(tong):
    tong, result,ti_le =choi(diem)
    save_to_csv([tong, result,ti_le])