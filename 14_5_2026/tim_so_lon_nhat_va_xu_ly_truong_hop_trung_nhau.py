
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))

# Tìm số lớn nhất
max_value = max(a, b, c)
print(f"Giá trị lớn nhất là: {max_value}")

# Kiểm tra điều kiện trùng giá trị lớn nhất
if a == b == c: # Trường hợp cả 3 số bằng nhau
    print(f"Cả 3 số bằng nhau, số còn lại (sau khi loại 2 số max) vẫn là: {a}")
# Các trường hợp chỉ có 2 số bằng max
elif a == b == max_value:
    print(f"Giá trị thứ ba còn lại là: {c}")
elif a == c == max_value:
    print(f"Giá trị thứ ba còn lại là: {b}")
elif b == c == max_value:
    print(f"Giá trị thứ ba còn lại là: {a}")