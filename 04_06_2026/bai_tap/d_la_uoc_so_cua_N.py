"""

Nhập số nguyên N, tạo một tập hợp các số nguyên dương d là ước số của N

"""

import math

def tim_uoc_so(n):
    # Sử dụng set để lưu trữ các ước số (tự động loại bỏ trùng lặp và sắp xếp lại nếu cần)
    uoc_so = set()
    
    # Lấy giá trị tuyệt đối vì đề bài yêu cầu ước số nguyên dương của N
    n = abs(n)
    
    if n == 0:
        return "Số 0 có vô số ước số nguyên dương."

    # Duyệt từ 1 đến căn bậc hai của n
    for i in range(1, int(math.isqrt(n)) + 1):
        if n % i == 0:
            uoc_so.add(i)       # i là ước số
            uoc_so.add(n // i)  # n // i cũng là ước số
            
    # Chuyển về list và sắp xếp tăng dần cho dễ nhìn
    return sorted(list(uoc_so))

# Nhập dữ liệu từ bàn phím
try:
    N = int(input("Nhập số nguyên N: "))
    ket_qua = tim_uoc_so(N)
    print(f"Tập hợp các ước số nguyên dương của {N} là: {ket_qua}")
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ!")