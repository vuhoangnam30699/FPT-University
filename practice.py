import math

"""1. Nhập một số nguyên n. Kiểm tra n là số dương, âm hay bằng 0 """

# n = int(input('Nhập n: '))
# 
# if n < 0:
#     print('n là số âm')
# elif n > 0:
#     print('n là số dương')
# else:
#     print('n = 0')
    
"""2. Nhập tuổi của một người. Nếu tuổi >= 18 thì in "Đủ tuổi", ngược lại in "Chưa đủ tuổi"."""

# age = int(input('Nhập tuổi của bạn: '))
# 
# if age < 18:
#     if age < 0:
#         print('????')
#     else:
#         print("Chưa đủ tuổi")
# else:
#     print("Đã đủ tuổi")


"""3. Nhập hai số a, b. In ra số lớn hơn."""

# a = float(input('Nhập a: '))
# b = float(input('Nhập b: '))
# 
# if a > b:
#     print(a)
# elif a < b:
#     print(b)
# else:
#     print('2 số bằng nhau')

"""4. Nhập một số nguyên. Kiểm tra số đó chẵn hay lẻ """

# n = int(input('Nhập n: '))
# 
# if n % 2 == 0:
#     print('là số chẵn')
# else:
#     print('là số lẻ')

"""

5. Nhập điểm trung bình. Xếp loại:
>= 8: Giỏi
>= 6.5: Khá
>= 5: Trung bình
< 5: Yếu

"""

# def dtb(n):
#     
#     if 0 <= n < 5:
#         print('Yếu')
#     elif 5 <= n < 6.5:
#         print('Trung bình')
#     elif 6.5 <= n < 8:
#         print('Khá')
#     elif 8 <= n <= 10:
#         print('Giỏi')
#     else:
#         print('????')
#         
# avg = int(input('Nhập điểm TB: '))
# 
# dtb(avg)


"""6. Nhập năm bất kỳ. Kiểm tra năm nhuận. """

# while True:
#     
#     y = int(input('Year: '))
#     
#     if y < 0:
#         print('Số năm phải > hoặc = 0. Vui lòng nhập lại!')
#         continue
#     elif (y % 4 == 0 and y % 100 != 0):
#         print(f'{y} là năm nhuận')
#         break
#     else:
#         print (f'{y} không phải là năm nhuận')
#         break

"""7. Nhập 3 số a, b, c. Tìm số lớn nhất. """

# a = int(input('Nhập a: '))
# b = int(input('Nhập b: '))
# c = int(input('Nhập c: '))
# 
# 
# max_number = max(a, b, c)
# 
# print(f"Số lớn nhất là: {max_number}")

"""8. Nhập tháng. In số ngày của tháng đó."""

# while True:
#     
#     m = int(input('Nhấp tháng bạn muốn kiểm tra: '))
#     
#     if m in [1, 3, 5, 7, 8, 10, 12]:
#         print(f'Tháng {m} có 31 ngày')
#         break
#     elif m in [4, 6, 9, 11]:
#         print(f'Tháng {m} có 30 ngày')
#         break
#     elif m == 2:
#         y = int(input('Nhập năm: '))
#         if y < 0:
#             print('Số năm phải > hoặc = 0. Vui lòng nhập lại!')
#             continue
#         elif (y % 4 == 0 and y % 100 != 0):
#             print(f'Vì Tháng 2 năm {y} có 29 ngày')
#             break
#         else:
#             print (f'Tháng 2 năm {y} có 28 ngày')
#             break
#     else:
#         print('Không hợp lệ! Nhập lại!')
#         continue


"""9. In các số từ 1 đến 10 bằng vòng lặp for"""

# for n in range(0, 10):
#     print(n+1)

"""10. In các số chẵn từ 0 đến 20 bằng range(n, m, k)."""

# for n in range (0, 21, 2):
#     print(n)

"""11. Tính tổng các số từ 1 đến n."""

"""Cách 1"""
# def total(n):
#     return n * (n + 1) // 2
# 
# print(total(100))

"""Cách 2"""
# def total(n):
#     return sum(range(1, n + 1))
# 
# print(total(100))

"""Cách 3"""
# def total(n):
#     t = 0
#     for i in range(1, n + 1):
#         t += i
#     return t
# 
# print(total(100))

"""12. Tính tích: 1 * 2 * 3 * ... * n """

"""Cách 1"""

# def tich(n):
#     t = 1
#     for i in range(1, n + 1):
#         t *= i
#     return t
# 
# print(tich(3))

"""Cách 2"""

# def tich(n):
#     
#     if n <= 1:
#         return 1
#     
#     return n * tich(n - 1) # Công thức đệ quy: n! = n * (n-1)!
# 
# print(tich(3))

"""Cách 3"""

# n = int(input('n = '))
# print(math.factorial(n))


"""13. In bảng cửu chương của số n."""

# def bang_cuu_chuong(n):
#     for i in range(1, 11):  
#         ket_qua = n * i
#         
#         print(f"{n} x {i:2d} = {ket_qua:2d}")
# 
# bang_cuu_chuong(5)

"""14. Đếm có bao nhiêu số chia hết cho 3 trong đoạn từ 1 → 100."""

# c = 0
# 
# for n in range(1, 101):
#     if n % 3 == 0:
#         c +=1
#     
# print(c)

"""15. In các số từ 10 về 1."""

# for n in range (10, 0, -1):
#     print(n)

"""16. In các ký tự trong chuỗi "Python" bằng vòng lặp for."""

# s ='Python'
# 
# for i in s:
#     print(i)

"""17. Tính tổng các số chẵn từ 1 → n."""


"""Cách 1"""

# def tong_so_chan(n):
#     t = 0
#     
#     for i in range(1, n + 1):
#         if i % 2 == 0:
#             t += i
#     return t
#     
# n = int(input('n = '))
# print(tong_so_chan(n))

"""Cách 2"""

# def tong_so_chan(n):
#     return sum(range(2, n + 1, 2))
# 
# n = int(input('n = '))
# print(tong_so_chan(n))


"""18. In tam giác vuông. Ví dụ n = 4"""

# n = int(input('n = '))
# 
# for i in range(1, n + 1):
#     print('*' * i)

"""19. Dùng while in các số từ 1 → 10."""

# n = 1
# 
# while n <= 10:
#     print(n)
#     n += 1

"""20. Tính tổng từ 1 → n bằng while."""

# while True:
#     n = int(input('n = '))
#     if n >= 1:
#         break 
#     print('Nhập lại! n phải lớn hơn hoặc bằng 1')
# 
# 
# t = 0
# for i in range(1, n + 1):
#     t += i
# 
# print(t)

"""21. Nhập mật khẩu. Nếu sai thì yêu cầu nhập lại cho đến khi đúng."""

# password = 'Abcd1234@'
# 
# while True:
#     password_verify = input('Password: ')
#     
#     if password_verify == password:
#         print('Success!')
#         break
#     else:
#         print('Wrong Password! Please try again.')

"""22. Nhập các số liên tục. Dừng khi nhập số 0. Tính tổng các số đã nhập."""

# t = 0
# 
# while True:
#     n = int(input('Nhập số: '))
#     
#     if n == 0:
#         break
#     
#     t += n
#     
# print("Tổng các số đã nhập là:", t)


"""23. Đếm số chữ số của một số nguyên dương. Ví dụ: 12345 → 5 chữ số"""

"""Cách 1: try-catch"""

# while True:
#     try:
#         n = int(input('n = '))
#         if n <= 0:
#             print('Không hợp lệ! Yêu cầu nhập số nguyên dương')
#         else: 
#             c = len(str(n))
#             print(f'{n} -> {c} chữ số')
#             break
#     except ValueError:
#         print('Không hợp lệ! Yêu cầu nhập số nguyên dương')

"""Cách 2: isdigit()"""

# while True:
#     s = input('n = ') 
#     if not s.isdigit() or s == '0':
#         print('Không hợp lệ! Yêu cầu nhập số nguyên dương')       
#     else:   
#         c = len(s)
#         print(f'{s} -> {c} chữ số')
#         break
    
"""24. Đảo ngược số nguyên. Ví dụ: 1234 → 4321"""

"""Cách 1"""

# while True:
#     s = input('Nhập số nguyên n = ').strip()
#     
#     # Kiểm tra tính hợp lệ (phải là số nguyên, chấp nhận cả dấu âm)
#     # Loại bỏ dấu trừ ở đầu (nếu có) trước khi dùng .isdigit()
#     s_kiem_tra = s[1:] if s.startswith('-') else s
#     
#     if not s_kiem_tra.isdigit() or s == '-' or s == '':
#         print('Không hợp lệ! Vui lòng nhập một số nguyên.')
#     else:
#         # Xử lý đảo ngược
#         if s.startswith('-'):
#             # Nếu là số âm: giữ dấu trừ, đảo ngược phần số phía sau
#             so_dao = '-' + s[1:][::-1]
#         else:
#             # Nếu là số dương: đảo ngược toàn bộ
#             so_dao = s[::-1]
#             
#         # Chuyển về kiểu int để mất các số 0 thừa ở đầu (ví dụ: 0021 -> 21)
#         print(f'{s} -> {int(so_dao)}')
#         break


"""Cách 2"""

# while True:
#     try:
#         n = int(input('Nhập số nguyên n = '))
#         break
#     except ValueError:
#         print('Không hợp lệ! Vui lòng nhập một số nguyên.')
# 
# # Tiến hành đảo ngược bằng toán học
# dau = 1 if n >= 0 else -1
# so_goc = abs(n)
# so_dao = 0
# 
# while so_goc > 0:
#     chu_so_cuoi = so_goc % 10          # Lấy chữ số cuối cùng
#     so_dao = so_dao * 10 + chu_so_cuoi # Đẩy các số cũ sang trái và cộng số mới vào
#     so_goc //= 10                      # Cắt bỏ chữ số cuối cùng
# 
# ket_qua_cuoi = so_dao * dau
# print(f'{n} -> {ket_qua_cuoi}')
    
    
"""25. Viết hàm: def hello() In ra "Hello Python". """

# def hello():
#     print('Hello Python')
#     
# hello()

"""26. Viết hàm tính tổng 2 số. Ví dụ: sum2(3, 5) -> Kết quả: 8 """

# def sum2(a, b):
#     print(a + b)
#     
# a = int(input('a: '))
# b = int(input('b: '))
# 
# sum2(a,b)

"""27. Viết hàm kiểm tra số chẵn is_even(n). Trả về True hoặc False. """

# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
#     
# n = int(input('n: '))
# 
# print(is_even(n))

"""28. Viết hàm tính giai thừa factorial(n)"""

# def factorial(n):
#     
#     if n < 0:
#         return 'Giai thừa phải lớn hơn hoặc bằng 0'
#     
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
# 
# 
# n = int(input('n: '))
# 
# print(factorial(n))

"""

29. Viết hàm đếm số nguyên âm trong danh sách.
Ví dụ: [-1, 2, -5, 7]
Kết quả: 2

"""

# def dem_so_am(danh_sach):
#     count = 0
#     for num in danh_sach:
#         if num < 0:
#             count += 1
#     return count
# 
# 
# numbers = [-1, 2, -5, 7]
# print(dem_so_am(numbers))


"""

30. Viết hàm kiểm tra số nguyên tố.
is_prime(n)
Trả về True nếu là số nguyên tố, ngược lại False.

"""

# def is_prime(n):
#     # Lọc các trường hợp đặc biệt nhỏ hơn hoặc bằng 1
#     if n <= 1:
#         return False
#         
#     # Số 2 là số nguyên tố chẵn duy nhất
#     if n == 2:
#         return True
#         
#     # Loại bỏ các số chẵn lớn hơn 2 để giảm một nửa số lần lặp
#     if n % 2 == 0:
#         return False
#         
#     # Kiểm tra các số lẻ từ 3 đến căn bậc hai của n
#     # Bước nhảy là 2 (3, 5, 7, 9...) vì ta đã loại số chẵn ở trên
#     can_bac_hai = int(math.sqrt(n))
#     for i in range(3, can_bac_hai + 1, 2):
#         if n % i == 0:
#             return False  # Tìm thấy ước số khác -> Không phải số nguyên tố
#             
#     return True  # Không tìm thấy ước số nào -> Là số nguyên tố
# 
# 
# n = int(input('n: '))
# 
# print(is_prime(n))






    

    


    