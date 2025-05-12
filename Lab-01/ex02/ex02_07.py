#Nhập các dòng từ người    dùng
print("Nhập các dòng văn bản (nhập 'STOP' để dừng):")
lines = []
while True:
    line = input()
    if line == "STOP":
        break
    lines.append(line)
    #Chuyển các dòng thàng chữ hoa và in ra
    print("\nCác dòng đã nhập sau khi chuyển thành chữ hoa:")
for line in lines:
        print(line.upper())