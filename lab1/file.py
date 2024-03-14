#Bài 1
print("""
i carry your heart with me (i carry it in
my heart) i am never without it (anywhere
i go you go, my dear; and whatever is done
by only me is your doing, my darling)
i fear no fate (for you are my fate, my sweet)
i want no world (for beautiful you are my world, my true)
and it's you are whatever a moon has always meant
and whatever a sun will always sing is you
      
here is the deepest secret nobody knows
(here is the root of the root and the bud of the bud
and the sky of the sky of a tree called life; which grows
higher than soul can hope or mind can hide)
and this is the wonder that's keeping the stars apart
      
i carry your heart (i carry it in my heart)
---i carry your heart with me by e.e. cummings---  
""")
#Bài 2
so=int(input("Nhập số lượng sách : "))
ma=int(input("Nhập mã sách : "))
ten=input("Nhập tên sách : ")
tac_gia=input("Nhập tên tác giả : ")
xuatban=int(input("Nhập năm xuất bản : "))
print(f"""Thư viện ĐHKTKTCN có {so} sách {ten} với mã số {ma}. 
Cuốn sách của tác giác {tac_gia} được xuất bản vào năm {xuatban}
""")
#Bài 3
#1)
amount_after_5_years=10000*1.06**5
print("số tiền sẽ có sau 5 năm là {:.2f}".format(amount_after_5_years))
#2
amount_after_10_years=10000*1.06**10
print("số tiền sẽ có sau 10 năm là {:.2f}".format(amount_after_10_years))
#3
tangtruong=(amount_after_10_years/amount_after_5_years -1 )*100
print("tỉ lệ tăng trưởng sau 10 năm so với 5 năm là {:.2f} %".format(tangtruong))
#Bài 4
d,h=map(int,input("Nhập độ dài cạnh đáy và chiều cao của chóp tứ giác : ").split())
P_day=d*4     #Chu vi đáy
S_day=d*d     #Diện tích đáy
Sxq=P_day*h/2
Stp=Sxq+S_day
V=(1/3)*S_day*h
print("Diện tích xung quan là {:.2f}. Diện tích toàn phần là {:.2f}.Thể tích là {:.2f}".format(Sxq,Stp,V))
#Bài 5
so_gio=float(input("thời gian sử dụng máy lọc : "))
P=220*1.5   #công suất tiêu thụ
E=P*so_gio   # năng lượng tiêu thụ
tien_dien= (E/1000)*5000
print("Số tiền điện phải trả sau {} giờ là {} đồng".format(so_gio,tien_dien))
#Bài 6
a1,b1=map(int,input("Nhập tọa độ vector A : ").split())
a2,b2=map(int,input("Nhập tọa độ vector B : ").split())
# cộng 2 vector
tong=(a1+a2,b1+b2)
print(f"vector (A+B) = {tong}")
# trừ 2 vector
hieu=(a1-a2,b1-b2)
print(f"vector (A-B) = {hieu}")
# độ dài vector a , b
a_cm=(a1**2 + b1**2)**0.5
b_cm=(a2**2 + b2**2)**0.5
print(f"Độ dài vector A là : {a_cm}")
print(f"Độ dài vector B là : {b_cm}")
#cosin góc giữa 2 vector a và b
import math
CosAB=(a1*a2+b1*b2)/(math.sqrt(a1**2 + b1**2)*math.sqrt(a2**2 + b2**2))
print("Góc xen giữa A và B là : {:.2f}".format(CosAB))


#Bài 7
a1,b1,c1=map(float,input("nhập lần lượt hệ số của phương trình dạng a1,b1,c1: ").split())
a2,b2,c2=map(float,input("nhập lần lượt hệ số của phương trình dạng a2,b2,c2: ").split())
he_so_nhan=a2/a1 
a1_=a1*he_so_nhan
b1_=b1*he_so_nhan
c1_=c1*he_so_nhan
y=(c2-c1_)/(b2-b1_)
x=(c1-b1*y)/a1
print ("vậy nghiệm của hệ phương trình trên là: x={},y={}".format(round(x,2),round(y,2)))

#Bài 8
import math
x,z=map(int,input("Nhập số vào : ").split())
tu=(x**2)*math.sin(z)+(abs(x))**0.5
mau=math.log(z)+2.71**(x-1)
unstoppable=tu/mau + math.atan(x*z) 
print("giá trị của biểu thức là {:.2f}".format(unstoppable))
#bài 9
xM,yM=map(int,input("Nhập tọa độ đỉnh M : ").split())
xN,yN=map(int,input("Nhập tọa độ đỉnh N : ").split())
xP,yP=map(int,input("Nhập tọa độ đỉnh P : ").split())
xQ,yQ=map(int,input("Nhập tọa độ đỉnh Q : ").split())
td_MN=((xM+xN)/2,(yM+yN)/2)
td_NP=((xN+xP)/2,(yN+yP)/2)
td_PQ=((xP+xQ)/2,(yP+yQ)/2)
td_QM=((xQ+xM)/2,(yQ+yM)/2)
print("trung điểm của MN= {},NP= {},PQ= {},QM= {}".format(td_MN,td_NP,td_PQ,td_QM))
#Bài 10
def giaithua(n):           
 list1=[n]
 a=n
 for i in range (n): 
        a=a-1
        if a==0:
                break
        list1.append(a)
 tich=1
 for i in list1:
      tich=tich*i
 return float(tich)

 
bi=int (input("nhập số bi muốn rút ra : "))
khong_gian_mau_ckn= (giaithua(50)/(giaithua(50-bi)))     #tính không gian mẫu theo công thức tổng quát 
#1 tính xs rút đc all bi đỏ 
if bi<=20: 
 tat_ca_bi_mau_do=(giaithua(20)/(giaithua(20-bi)))           
 xs_all_red=tat_ca_bi_mau_do/khong_gian_mau_ckn
 print ("xác suất rút đc tất cả bi đều là màu đỏ là :",xs_all_red)
else :
    print("số lượng bi đỏ chỉ có tối đa 20")

#2 tính xs rút đc ít nhất 1 bi xanh 
tat_ca_bi_khong_phai_mau_xanh=(giaithua(35)/(giaithua(35-bi)))    #ít nhất 1 bi xanh tương đương phần bù của không có viên bi xanh nào 
xs_no_blue=tat_ca_bi_khong_phai_mau_xanh/khong_gian_mau_ckn
xs_it_nhat_1_vien_mau_xanh=1-xs_no_blue
print ("xác suất để rút đc ít nhất một bi màu xanh là: ",xs_it_nhat_1_vien_mau_xanh)
#3 tính xs rút đc đúng 2 bi vàng 
xs_rut_1_bi_vang=((giaithua(15)/(giaithua(15-1)))/(giaithua(50)/(giaithua(50-1))))    
xs_rut_dc_dung_2bivang=xs_rut_1_bi_vang*xs_rut_1_bi_vang                 #áp dụng quy tắc nhân xác suất
print ("xác suất rút đc đúng 2 bi vàng là:",xs_rut_dc_dung_2bivang)