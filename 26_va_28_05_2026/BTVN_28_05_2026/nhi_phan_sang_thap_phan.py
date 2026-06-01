""" 2. Người dùng nhập từ bàn phím chuỗi các số nhị phân viết liên tiếp được nối nhau bởi dấu phẩy.
Hãy nhập chuỗi đầu vào sau đó in ra những giá trị được nhập.

"""

c = input('Nhập các số nhị phân (cách nhau bởi dấu phẩy): ')

# Tách chuỗi và loại bỏ khoảng trắng thừa
danh_sach_nhi_phan = [item.strip() for item in c.split(',')]

# Cách 1: In ra các chuỗi nhị phân nguyên bản (Giống code của bạn)
print("Các chuỗi nhị phân đã nhập:", danh_sach_nhi_phan)

# Cách 2: Chuyển đổi và in ra giá trị thập phân tương ứng (Nên làm theo cách này)
gia_tri_thap_phan = []
for item in danh_sach_nhi_phan:
    if item: # Kiểm tra tránh trường hợp chuỗi rỗng do nhập thừa dấu phẩy
        so_thap_phan = int(item, 2) # Tham số 2 nghĩa là hiểu chuỗi này ở hệ cơ số 2
        gia_tri_thap_phan.append(so_thap_phan)

print("Giá trị thập phân tương ứng là:", gia_tri_thap_phan)