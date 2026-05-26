# Kiểm tra 1 số dương N có phải số fibonacci không?

n = int(input("Nhập số dương N: "))

f0, f1 = 0, 1

while f1 != n:
    if f1 > n:		#Nếu f1> n thì thoát vòng lặp
        break
    f0, f1 = f1, f0 + f1  # f0 = f1, f1 = f0 + f1
print ('Fibonacci' if f1 == n else 'Non-fibonacci')