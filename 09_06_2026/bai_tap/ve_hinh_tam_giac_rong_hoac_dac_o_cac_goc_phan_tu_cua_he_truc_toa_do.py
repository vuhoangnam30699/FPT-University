"""
Vẽ hình tam giác rỗng (đặc) (sử dụng các ký hiệu dấu *) ở các góc phần tư I, II, III, IV của hệ trục tọa độ.

"""

def tao_dong_tam_giac(y_pos, n, loai):
    """Hàm tạo ra chuỗi ký tự cho một nửa dòng bên phải (Góc I hoặc IV)"""
    chieu_rong = n - y_pos + 1

    if loai == "dac":
        phan_tu = "*" * chieu_rong
    else:  # loai == 'rong'
        if y_pos == 1:  # Đường đáy nằm sát trục hoành
            phan_tu = "*" * n
        elif y_pos == n:  # Đỉnh tam giác
            phan_tu = "*"
        else:  # Các đường thân ở giữa
            phan_tu = "*" + " " * (chieu_rong - 2) + "*"

    # Căn lề phải để đảm bảo độ rộng thống nhất là N
    return phan_tu.ljust(n)


# --- CHƯƠNG TRÌNH CHÍNH ---

# Nhập kích thước N
while True:
    try:
        n = int(input("Nhập kích thước tam giác (N >= 2): "))
        if n < 2:
            print("Kích thước quá nhỏ để tạo hình rỗng. Vui lòng nhập lại!")
            continue
        break
    except ValueError:
        print("Lỗi: Vui lòng nhập một số nguyên hợp lệ!")

# Chọn loại tam giác (Đặc hoặc Rỗng)
while True:
    loai = (
        input("Bạn muốn vẽ tam giác Đặc hay Rỗng? (nhập 'dac' hoặc 'rong'): ")
        .strip()
        .lower()
    )
    if loai in ["dac", "rong"]:
        break
    print("Lựa chọn không hợp lệ. Vui lòng chỉ nhập 'dac' hoặc 'rong'!")

print("\n--- KẾT QUẢ ĐỒ THỊ ---\n")

# Thuật toán vẽ hệ trục tọa độ từ Y = N xuống Y = -N
for y in range(n, -n - 1, -1):
    # Trường hợp trục hoành (Y = 0)
    if y == 0:
        print("-" * n + "+" + "-" * n)
        continue

    # Lấy giá trị tuyệt đối của Y để tính toán khoảng cách tới trục hoành
    y_pos = abs(y)

    # Tạo phần bên phải (Góc I nếu y > 0, Góc IV nếu y < 0)
    ve_phai = tao_dong_tam_giac(y_pos, n, loai)

    # Phần bên trái là hình đối xứng (đảo ngược) của phần bên phải
    ve_trai = ve_phai[::-1]

    # Ghép lại với nhau qua trục tung '|'
    print(ve_trai + "|" + ve_phai)