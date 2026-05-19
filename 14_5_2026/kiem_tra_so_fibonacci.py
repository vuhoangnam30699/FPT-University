def isFibo(N):
   
    if N < 0:
        return False
    
    # Khởi tạo 2 số đầu tiên của dãy Fibonacci
    a, b = 0, 1
    while a < N:
        a, b = b, a + b
        
    # Nếu tìm thấy số bằng N thì True, ngược lại False
    return a == N


print(isFibo(8))   # True
print(isFibo(10))  # False