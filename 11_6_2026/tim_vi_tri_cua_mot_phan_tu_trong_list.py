"""

Tìm vị trí của một phần tử trong list:
• Yêu cầu người dùng nhập vào số lượng phần tử của list.
• Nhập giá trị cho từng phần tử.
• Yêu cầu nhập giá trị cần tìm.
• Tìm và in ra tất cả các vị trí của giá trị cần tìm trong list.

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
        
# Yêu cầu nhập giá trị cần tìm
while True:
    try:
        can_tim = float(input("Nhập giá trị cần tìm: "))
        break
    except ValueError:
        print("Lỗi: Giá trị cần tìm phải là một số!")

# Tìm tất cả các vị trí (index) của giá trị đó
# Sử dụng List Comprehension để duyệt qua từng phần tử và lấy ra index nếu khớp
vi_tri_tim_thay = [index for index, value in enumerate(danh_sach) if value == can_tim]


print("\n")
print(f"List: {danh_sach}")

if vi_tri_tim_thay:
    print(f"Tìm thấy giá trị {can_tim} tại các vị trí:")
    for idx in vi_tri_tim_thay:
        # idx là chỉ số trong lập trình (bắt đầu từ 0)
        # idx + 1 là vị trí thứ tự thực tế ngoài đời (bắt đầu từ 1)
        print(f"- Index {idx} (Vị trí thứ {idx + 1} trong list)")
else:
    print(f"Không tìm thấy giá trị {can_tim} nào trong list.")
        
