chuoi_nhap = input("Nhập dãy số (cách nhau bởi dấu chấm phẩy ';'): ")

# 1. Tách chuỗi dựa vào dấu ';'
# 2. Loại bỏ khoảng trắng thừa và ép sang kiểu int
danh_sach_so = [int(x.strip()) for x in chuoi_nhap.split(';') if x.strip()]

# Đưa danh sách vào set để loại bỏ các số trùng lặp
tap_hop_so = set(danh_sach_so)

print("Số lượng các số khác nhau trong dãy là:", len(tap_hop_so))