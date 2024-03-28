#a
for i in range(100,1001):
    check=True
    for j in range(2,i):
        if i%j==0:
            check=False
    if check==True:
        print(i,end=",")
#b
scp=0
for i in range (1,1001):
    for j in range (1,i):
        if j==i**(1/2):
            scp=i
    if i==scp:
        print (i,end=",")
#c em không biết làm
#d
for i in range(1,500):
    sum=0
    for j in range(1,i):
        if i%j==0:
            sum=sum+j
    if sum==i:
        print(i)
#e
tong=0
for i in range(1,201):
    a=i*(3*i-1)/2
    tong+=a
print(tong)
