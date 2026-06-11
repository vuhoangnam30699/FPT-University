
last_val = None             # Lưu số vừa nhập ở lượt trước
consecutive_same_count = 0  # Đếm số lần nhập lặp lại liên tiếp
consecutive_even_count = 0  # Đếm số lần nhập số chẵn liên tiếp

print("--- CHƯƠNG TRÌNH NHẬP SỐ NGUYÊN DƯƠNG ---")

while True:
    try:
        user_input = input("Nhập một số nguyên dương (Nhập 0 để dừng): ")
        
        # 1. Kiểm tra nếu chuỗi nhập vào không phải là số nguyên
        try:
            val = int(user_input)
        except ValueError:
            raise Exception("Lỗi nhập số")
        
        # 2. Kết thúc bình thường khi người dùng nhập số 0
        if val == 0:
            print("Chương trình kết thúc bình thường. Tạm biệt!")
            break
            
        # 3. Kiểm tra nếu người dùng nhập số âm
        if val < 0:
            raise Exception("Lỗi số âm!!!")
            
        # --- CẬP NHẬT TRẠNG THÁI ĐỂ KIỂM TRA ĐIỀU KIỆN LIÊN TIẾP ---
        
        # Xử lý đếm số giống nhau liên tiếp
        if last_val is not None and val == last_val:
            consecutive_same_count += 1
        else:
            consecutive_same_count = 1
            
        # Xử lý đếm số chẵn liên tiếp
        if val % 2 == 0:
            consecutive_even_count += 1
        else:
            consecutive_even_count = 0
            
        # 4. Kiểm tra điều kiện nhập lặp 4 lần liên tiếp
        if consecutive_same_count == 4:
            consecutive_same_count = 0  # Reset bộ đếm lặp
            last_val = None             # Xóa dấu vết để lượt sau tính lại từ đầu
            raise Exception("Lỗi nhập lặp")
            
        # 5. Kiểm tra điều kiện nhập 5 số chẵn liên tiếp
        if consecutive_even_count == 5:
            consecutive_even_count = 0  # Reset bộ đếm chẵn
            raise Exception("Lỗi nhập chẵn")
            
        # Nếu không có lỗi nào xảy ra, cập nhật số cuối cùng hợp lệ
        last_val = val

    except Exception as e:
        # Bắt mọi exception được raise ở trên, in thông báo ra màn hình
        print(f"-> Error: {e}")
        # Vòng lặp while True không bị ngắt, chương trình tiếp tục hoạt động bình thường