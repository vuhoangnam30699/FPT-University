"""

Đảo ngược list:
• Yêu cầu người dùng nhập vào số lượng phần tử của list.
• Nhập giá trị cho từng phần tử.
• Đảo ngược list và in ra list đã đảo ngược.

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
        

# Đảo ngược danh sách
danh_sach_dao_nguoc = danh_sach[::-1]


print("\n")
print(f"List: {danh_sach}")
print(f"List đảo ngược: {danh_sach_dao_nguoc}")

