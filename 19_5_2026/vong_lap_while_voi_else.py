# nhập số n và kiểm tra xem có phải số nguyên tố hay không
# chú ý: nếu không sử dụng else, ta phải khai báo thêm biến phụ và chương trình dài hơn vài dòng       


n = int(input("Nhập số N: "))
x =2
while x < n:
    if (n % x) == 0:
        print("N không phải số nguyên tố")
        break
    x = x + 1
else:
    print("N là số nguyên tố")