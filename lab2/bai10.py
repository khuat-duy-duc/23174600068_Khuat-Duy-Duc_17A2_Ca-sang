chon=(input("Mời bạn lựa chọn thể loại phim : "))
gio=input("mời bạn nhập thời gian xem (sáng,trưa,chiều,tối) : ")
if chon=="Hành động":
    if gio=="sáng":
        print("Bạn chọn thể loại Hành động ,thơi gian chiếu phim là 8 giờ 50 phút")
    elif gio=="trưa":
        print("Bạn chọn thể loại Hành động ,thời gian chiếu phim là 12 giờ 30 phút")
    elif gio=="chiều":
        print("Bạn chọn thể loại Hành động ,thời gian chiếu phim là 16 giờ ")
    elif gio=="tối":
        print("Bạn chọn thể loại Hành động ,thời gian chiếu phim là 22 giờ")
elif chon=="Kinh dị":
    if gio=="tối":
        print("Bạn chọn thể loại Kinh dị, thời gian chiếu phim là 21 giờ")
    else:
        print("Không có suất chiếu")
elif chon=="Tình cảm":
    if gio=="tối":
        print("Bạn chọn thể lại Tình cảm,thời gian chiếu phim là 20 giờ 30p phút")
    else:
        print("Không có suất chiếu")
elif chon=="Hài hước":
    if gio=="sáng":
        print("Bạn đã chọn thể loại hài hước,thời gian chiếu phim là 9 giờ")
    elif gio=="trưa":
        print("Bạn đã chọn thể loại Hài hước,thời gian chiếu phim là 11 giờ")
    elif gio=="chiều":
        print("Bạn đã chọn thể loại Hài hước,thời gian chiếu phim là 16 giờ 30 phút")
    elif gio=="tối":
        print("Bạn đã chọn thể loại Hài hước,thời gian chiếu phim là 23 giờ")
elif chon=="Hoạt hình":
    if chon=="sáng":
        print("Bạn đã chọn thể loại Hoạt hình, thời gian chiếu phim là 8 giờ")
    elif chon=="trưa":
        print("Bạn đã chọn thể loại Hoạt hình, thời gian chiếu phim là 13 giờ")
    else:
        print("Không có suất chiếu")