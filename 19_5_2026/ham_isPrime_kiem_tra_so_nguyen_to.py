# Viết hàm isPrime kiểm tra xem N có phải là số nguyên tố hay không?

import math

def isPrime(n):
    # Số nhỏ hơn hoặc bằng 1 không phải là số nguyên tố
    if n <= 1:
        return False
    
    # Kiểm tra từ 2 đến căn bậc hai của n
    i = 2
    while i <= math.isqrt(n):
        if n % i == 0:
            return False  # Nếu chia hết thì không phải số nguyên tố
        i += 1
        
    return True  # Nếu không chia hết cho số nào thì là số nguyên tố


while True:
    s = input("Nhập số cần kiểm tra: ")
    try:
        num = int(s)
    except ValueError:
        try:
            f = float(s)
            if f.is_integer():
                num = int(f)
            else:
                print('Vui lòng nhập một số nguyên (không nhập số thập phân).')
                continue
        except ValueError:
            print('Giá trị nhập không hợp lệ. Vui lòng nhập một số nguyên.')
            continue

    # Nếu đến đây thì có num là số nguyên hợp lệ
    if isPrime(num):
        print(f"{num} là số nguyên tố.")
    else:
        print(f"{num} không phải là số nguyên tố.")
    break
