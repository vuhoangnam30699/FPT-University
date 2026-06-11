"""

Tìm giá trị lớn nhất và nhỏ nhất trong list
• Yêu cầu người dùng nhập vào số lượng phần tử của list.
• Nhập giá trị cho từng phần tử.
• Tìm và in ra giá trị lớn nhất và nhỏ nhất trong list.

"""



while True:
    try:
        n = int(input("Nhập vào số lượng phần tử của list: "))
        if n <= 0:
            print("Số lượng phần tử phải lớn hơn 0. Vui lòng nhập lại!")
            continue  # Quay lại đầu vòng lặp
        break  # Nhập đúng số nguyên dương thì thoát vòng lặp
    except ValueError:
        print("Lỗi: Vui lòng nhập vào một số nguyên hợp lệ!")

# Khởi tạo một list rỗng để chứa các giá trị
danh_sach = []

# Nhập giá trị cho từng phần tử
i = 0
while i < n:
    try:
        gia_tri = float(input(f"Nhập giá trị cho phần tử thứ {i + 1}: "))
        danh_sach.append(gia_tri)
        i += 1  # Chỉ tăng số thứ tự khi nhập thành công số hợp lệ
    except ValueError:
        print("Lỗi: Giá trị phải là số (nguyên hoặc thập phân). Vui lòng nhập lại phần tử này!")
        
print(f"\nList: {danh_sach}")

# Tìm Min, Max trong list
# lon_nhat = max(danh_sach)
# nho_nhat = min(danh_sach)

gtln = danh_sach[0]
gtnn = danh_sach[0]

for x in danh_sach[1:]:
    if x > gtln:
        gtln = x
    if x < gtnn:
        gtnn = x



print("\n")
print(f"Max: {gtln}")
print(f"Min: {gtnn}")