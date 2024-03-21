c,n=map(float,input("Nhập chiều cao và cân nặng : ").split())
BMI=n/(c**2)
if BMI<18.5:
    print("Gầy")
elif 18.5<=BMI<=24.9:
    print("Bình thường")
elif 25<=BMI<=29.9:
    print("Hơi béo")
elif BMI>=30:
    print("Béo")