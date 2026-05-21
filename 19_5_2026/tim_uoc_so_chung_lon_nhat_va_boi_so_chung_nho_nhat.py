"""

Nhập 2 số nguyên dương A và B, tính và in ra màn
hình ước số chung lớn nhất và bội số chung nhỏ nhất
của hai số đó

"""

A = int(input("Nhập số nguyên dương A: "))
B = int(input("Nhập số nguyên dương B: "))

# Lưu lại giá trị ban đầu để tính BSCNN
tich = A * B

# Thuật toán Euclid dùng vòng lặp while
a_temp = A
b_temp = B
while b_temp != 0:
    r = a_temp % b_temp
    a_temp = b_temp
    b_temp = r

uscln = a_temp
bscnn = tich // uscln

print(f"Ước số chung lớn nhất (USCLN) là: {uscln}")
print(f"Bội số chung nhỏ nhất (BSCNN) là: {bscnn}")