#Nhập số từ người dùng 
so = int(input("Nhập số nguyên: "))
#Kiểm tra số nguyên là số chẵn hay lẻ
if so % 2 == 0:
    print (so, "là số chẵn")
else:
    print (so, "không phải là số chẵn")