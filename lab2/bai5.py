n=int(input("Số người mua vé : "))
if n==1:
    print("Tổng tiền phải trả khi mua vé là 120000đ")
elif 2<=n<4:
    ve=n*120000-n*120000*0.05
    print(f"Tổng tiền phải trả khi mua vé là {ve}đ")
elif 4<=n<10:
    ve=n*120000-n*120000*0.1
    print(f"Tổng tiền phải trả khi mua vé là {ve}đ")
else:
    ve=n*120000-n*120000*0.2
    print(f"Tổng tiền phải trả khi mua vé là {ve}đ")