#Tạo một danh sách rỗng để lưu kết quả
results = []
#Duyệt qua tất cả các số trong đoạn từ 2000 đến 3200, kiểm tra xem số i có chia hết cho 7 và 
# không phải là bội của 5
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5) != 0:
        results.append(str(i))
print(','.join(results))