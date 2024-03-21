a,b,c=map(int,input("Nhập hệ số của đường thẳng ax+by+c=0 là : ").split())
x,y,r=map(int,input("Nhập tọa độ tâm và bán kính của đường tròn : ").split())
import math
khoang_cach=(abs(a*x+b*y+c))/(math.sqrt(a**2 + b**2))
if khoang_cach==r:
    print("Đường thẳng tiếp xúc với đường tròn")
elif khoang_cach>r:
    print("Đường thẳng nằm ngoài đường tròn")
elif khoang_cach<r:
    print("Đường thẳng cắt đường tròn")