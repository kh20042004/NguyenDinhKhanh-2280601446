def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]

input_str = input("Nhập chuỗi: ")
result = dao_nguoc_chuoi(input_str)
print("Chuỗi đảo ngược là:", result)    