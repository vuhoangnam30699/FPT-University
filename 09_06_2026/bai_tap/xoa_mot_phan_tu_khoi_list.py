"""

Xóa một phần tử khỏi list:
• Yêu cầu người dùng nhập vào số lượng phần tử của list.
• Nhập giá trị cho từng phần tử.
• Nhập giá trị cần xóa khỏi list.
• Xóa giá trị đó khỏi list và in ra list mới.

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
        print("Lỗi: Vui lòng nhập vào một số nguyên hợp lệ!")
        
print(f"\nList: {danh_sach}")

# Nhập giá trị cần xóa
while True:
    try:
        can_xoa = float(input("Nhập giá trị cần xóa khỏi list: "))
        break
    except ValueError:
        print("Lỗi: Giá trị cần xóa phải là một số!")

# Kiểm tra và tiến hành xóa
if can_xoa not in danh_sach:
    print(f"Kết quả: Giá trị {can_xoa} không tồn tại trong list. Không có gì để xóa.")
else:
    # Dùng vòng lặp while kết hợp .remove() để xóa tất cả các phần tử trùng giá trị
    """
    while can_xoa in danh_sach:
        danh_sach.remove(can_xoa)
    """
    # Chỉ giữ lại các phần tử khác với giá trị 'can_xoa'
    danh_sach = [x for x in danh_sach if x != can_xoa]


    print("\n")
    print(f"Xóa thành công giá trị: {can_xoa}")
    print(f"List mới: {danh_sach}")