"""

Viết chương trình cho phép người dùng nhập vào liên
tiếp một dãy số tự nhiên (không biết trước độ dài),
việc nhập dãy sẽ kết thúc khi người dùng nhập một số
âm hoặc số 0.
Sau khi kết thúc, in ra màn hình ước số chung lớn nhất
và bội số chung nhỏ nhất của tất cả các số vừa nhập
vào.


"""


# Hàm tìm USCLN của 2 số bằng vòng lặp while
def tim_uscln(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

# Hàm tìm BSCNN của 2 số
def tim_bscnn(a, b):
    if a == 0 or b == 0:
        return 0
    return (a * b) // tim_uscln(a, b)


danh_sach = []
print("Nhập dãy số tự nhiên (Nhập số <= 0 để kết thúc):")

while True:
    so = int(input("Nhập số: "))
    if so <= 0:
        break
    danh_sach.append(so)

# Kiểm tra xem người dùng có nhập số hợp lệ nào không
if len(danh_sach) == 0:
    print("Bạn chưa nhập số tự nhiên hợp lệ nào!")
else:
    # Khởi tạo giá trị ban đầu là phần tử đầu tiên trong dãy
    uscln_ = danh_sach[0]
    bscnn_ = danh_sach[0]
    
    # Duyệt qua các số còn lại bằng vòng lặp while
    i = 1
    while i < len(danh_sach):
        uscln_ = tim_uscln(uscln_, danh_sach[i])
        bscnn_ = tim_bscnn(bscnn_, danh_sach[i])
        i += 1

    print(f"Dãy số đã nhập: {danh_sach}")
    print(f"Ước số chung lớn nhất của dãy là: {uscln_}")
    print(f"Bội số chung nhỏ nhất của dãy là: {bscnn_}")