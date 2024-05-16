chuối= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#lọc số lẻ
def so_le(n):
    return n % 2 != 0
lọc_chuối1= list(filter(so_le,chuối))
print("Các số lẻ trong danh sách là:",lọc_chuối1)
#lọc số chẵn
def so_chan(n):
    return n % 2 == 0
lọc_chuối2= list(filter(so_chan,chuối))
print("Các số lẻ trong danh sách là:",lọc_chuối2)
#lọc lập phương 
def lap_phuong(n):
    return n ** 3
chuoi_lap_phuong= list(map(lap_phuong,chuối))
print("Danh sách các lập phương của các số ban đầu là:",chuoi_lap_phuong)
# dùng map và filter
number= filter(so_chan,chuối)
Numbers = map(lap_phuong,number)
list_numbers = list(Numbers)
print("Danh sách lập phương các số chẵn trong danh sách ban đầu là:",list_numbers)
#
def binhphuong(n):
    return n ** 2

so= filter(so_le,chuối)
sonhieu = map(binhphuong,so)
sonhieus = list(sonhieu)
print("Danh sách lập phương các số chẵn trong danh sách ban đầu là:",sonhieus)


