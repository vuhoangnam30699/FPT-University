S = input("Nhập chuỗi S: ")

# Tạo một chuỗi rỗng để chứa kết quả mới
S_moi = ""

# Duyệt qua từng ký tự trong chuỗi S
for ky_tu in S:
    # Nếu ký tự đó là chữ số
    if ky_tu.isdigit() == True:
        # Thay thế bằng dấu chấm hỏi
        S_moi = S_moi + "?"
    else:
        # Giữ nguyên ký tự ban đầu nếu không phải là số
        S_moi = S_moi + ky_tu

print("Chuỗi S sau khi thay thế:", S_moi)