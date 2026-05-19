while True:
    
    print("--- Nhập thông tin ngày X ---")
    d = int(input("Nhập ngày d: "))
    m = int(input("Nhập tháng m: "))
    y = int(input("Nhập năm y: "))

    # Kiểm tra năm, tháng có hợp lệ trước không
    if y < 1 or m < 1 or m > 12:
        print("Tháng hoặc năm không hợp lệ! Vui lòng nhập lại.\n")
        continue

    # Xác định số ngày tối đa của tháng m vừa nhập
    is_leap = (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
    
    if m in [1, 3, 5, 7, 8, 10, 12]:
        max_days = 31
    elif m in [4, 6, 9, 11]:
        max_days = 30
    else:  # Tháng 2
        max_days = 29 if is_leap else 28

    # Kiểm tra ngày d có nằm trong khoảng hợp lệ từ 1 đến max_days không
    if d < 1 or d > max_days:
        print(f"Ngày không hợp lệ! Tháng {m} năm {y} chỉ có từ 1 đến {max_days} ngày thôi.")
        print("Vui lòng nhập lại toàn bộ!\n")
        continue  # Bắt nhập lại từ đầu nếu sai
    
    # Nếu vượt qua tất cả các kiểm tra trên, thoát vòng lặp để tính ngày tiếp theo
    break

# Tính ngày tiếp theo
d += 1  # Tăng ngày lên 1

if d > max_days:
    d = 1      # Reset về ngày đầu tháng
    m += 1     # Tăng tháng lên 1
    if m > 12:
        m = 1  # Reset về tháng 1 năm sau
        y += 1 # Tăng năm lên 1


print("\n" + "="*30)
print(f"Ngày tiếp theo là: {d}/{m}/{y}")
print("="*30)