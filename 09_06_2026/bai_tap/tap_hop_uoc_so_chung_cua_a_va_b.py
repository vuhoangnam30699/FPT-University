a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
a_abs, b_abs = abs(a), abs(b)

# Tìm tập ước số của a và b
uoc_a = {i for i in range(1, a_abs + 1) if a_abs % i == 0}
uoc_b = {i for i in range(1, b_abs + 1) if b_abs % i == 0}

# Lấy phần giao của 2 tập hợp (các phần tử có ở cả 2 tập)
uoc_chung = uoc_a.intersection(uoc_b)
# Hoặc có thể viết ngắn gọn: uoc_chung = uoc_a & uoc_b

print(f"Tập hợp các ước số chung của {a} và {b} là: {uoc_chung}")