""" 5. Nhập n, in n dòng đầu tiên của tam giác pascal """

def in_tam_giac_pascal(n):
    if n <= 0:
        print("Vui lòng nhập n lớn hơn 0.")
        return

    dong_truoc = []
    
    for i in range(n):
        # Mỗi dòng i sẽ có i + 1 phần tử, khởi tạo ban đầu toàn số 1
        dong_hien_tai = [1] * (i + 1)
        
        # Tính toán các giá trị bên trong (nếu không phải phần tử đầu và cuối)
        for j in range(1, i):
            dong_hien_tai[j] = dong_truoc[j - 1] + dong_truoc[j]
        
        # Tạo khoảng trống ở đầu để căn lề tam giác cho cân đối
        khoang_trong = " " * (n - i - 1)
        
        # Chuyển các số thành chuỗi để in ra cách nhau bằng khoảng trắng
        chuoi_dong = " ".join(map(str, dong_hien_tai))
        
        print(khoang_trong + chuoi_dong)
        
        # Lưu lại dòng hiện tại để làm bàn đạp tính cho dòng kế tiếp
        dong_truoc = dong_hien_tai

# Nhập số dòng từ người dùng
try:
    n = int(input("Nhập số nguyên dương n: "))
    in_tam_giac_pascal(n)
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ!")
