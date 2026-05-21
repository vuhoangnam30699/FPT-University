# Viết chương trình nhập hai số A và B, in ra tất cả các số nguyên tố nằm trong khoảng [A, B]

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

A = int(input("Nhập số A: "))
B = int(input("Nhập số B: "))

print(f"Các số nguyên tố trong khoảng [{A}, {B}] là:")
current = A
while current <= B:
    if isPrime(current):
        print(current, end=" ")
    current += 1
print()