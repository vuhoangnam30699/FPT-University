""" 7. 

Tạo tuple P gồm các số nguyên tố nhỏ hơn 1 triệu

-> Số nguyên tố là số tự nhiên có 2 ước số là 1 và chính nó.

"""


def sang_eratosthenes(limit):
    # Khởi tạo mảng đánh dấu, mặc định ban đầu tất cả là True (đều là số nguyên tố)
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False # 0 và 1 không phải số nguyên tố
    
    # Bắt đầu sàng
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            # Triệt tiêu các bội số của i bắt đầu từ i*i
            for j in range(i * i, limit, i):
                is_prime[j] = False
                
    # Gom các số nguyên tố lại thành một tuple
    primes_tuple = tuple(so for so, tinh_chat in enumerate(is_prime) if tinh_chat)
    return primes_tuple

# Tạo tuple P gồm các số nguyên tố nhỏ hơn 1.000.000
P = sang_eratosthenes(1000000)

print(f"Số lượng số nguyên tố nhỏ hơn 1 triệu là: {len(P)}")

dau = ", ".join(map(str, P[:10]))
cuoi = ", ".join(map(str, P[-5:]))

print(f"Các số nguyên tố nhỏ hơn 1 triệu: {dau}, ..., {cuoi}")