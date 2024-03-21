n=int(input("Nhập vào số nguyên có 3 chữ số : "))
hangtram=n//100
hangchuc=(n//10)%10
donvi=n%10
if hangtram==1:
    doctram="one hundred"
elif hangtram==2:
    doctram="two hundred"
elif hangtram==3:
    doctram="three hundred"
elif hangtram==4:
    doctram="four hundred"
elif hangtram==5:
    doctram="five hundred"
elif hangtram==6:
    doctram="six hundred"
elif hangtram==7:
    doctram="seven hundred"
elif hangtram==8:
    doctram="eight hundred"
elif hangtram==9:
    doctram="nine hundred"


if hangchuc==1:
    if donvi==1:
        docchuc="eleven"
    elif donvi==2:
        docchuc="twelve"
    elif donvi==3:
        docchuc="thirteen"
    elif donvi==4:
        docchuc="fourteen"
    elif donvi==5:
        docchuc="fifteen"
    elif donvi==6:
        docchuc="sixteen"
    elif donvi==7:
        docchuc="seventeen"
    elif donvi==8:
        docchuc="eighteen"
    elif donvi==9:
        docchuc="nineteen"
elif hangchuc==2:
    docchuc="twenty"
elif hangchuc==3:
    docchuc="thirty"
elif hangchuc==4:
    docchuc="forty"
elif hangchuc==5:
    docchuc="fifty"
elif hangchuc==6:
    docchuc="sixty"
elif hangchuc==7:
    docchuc="seventy"
elif hangchuc==8:
    docchuc="eighty"
elif hangchuc==9:
    docchuc="ninety"

if hangchuc!=1:
    if donvi==1:
       docvi="one"
    elif donvi==2:
       docvi="two"
    elif donvi==3:
       docvi="three"
    elif donvi==4:
       docvi="four"
    elif donvi==5:
       docvi="five"
    elif donvi==6:
       docvi="six"
    elif donvi==7:
       docvi="seven"
    elif donvi==8:
       docvi="eight"
    elif donvi==9:
       docvi="nine"   
else:
    docvi=""    


print(f"Số {n} đọc là : ",doctram,docchuc,docvi)