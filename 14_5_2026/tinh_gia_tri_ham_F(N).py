import math

N = int(input("Nhập số nguyên dương N: "))

F = 0
for i in range(1, N + 1):
    F += math.factorial(i)  # math.factorial(i) tính i!

print(f"Giá trị của F({N}) = {F}") # Công thức: F(N) = 1! + 2! + ... + N!