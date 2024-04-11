str1="Hello"
str2="World"
chuoi1=len(str1)
chuoi2=len(str2)
banana=""
lennao=chuoi1+chuoi2
for i in range(lennao):
    if i<chuoi1:
        banana+=str1[i] + "-"
    if i<chuoi2:
        banana+=str2[i] + "-"
lemon=banana[:-1]
print(lemon)

