N = int(input("Nhập số nguyên N: "))
N_abs = abs(N) # Lấy giá trị tuyệt đối để tìm ước dương

# Tạo tập hợp d gồm các số i từ 1 đến N mà N chia hết cho i
d = {i for i in range(1, N_abs + 1) if N_abs % i == 0}

print(f"Tập hợp các ước số dương của {N} là: {d}")