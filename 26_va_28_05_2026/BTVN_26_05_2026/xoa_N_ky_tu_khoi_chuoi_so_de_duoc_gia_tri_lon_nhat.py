# Nhập chuỗi S và số nguyên N
S_ban_dau = input("Nhập chuỗi số S: ")
N = int(input("Nhập số ký tự cần xóa N: "))

# Kiểm tra xem N có hợp lệ không (N phải từ 0 trở lên)
if N < 0:
    print("Lỗi: Số lượng ký tự cần xóa không thể là số âm!")
else:
    # Lọc sạch ký tự chữ, giữ lại duy nhất chữ số
    S = ""
    for ky_tu in S_ban_dau:
        if ky_tu.isdigit() == True:
            S = S + ky_tu

    # -Kiểm tra số lượng chữ số có đủ để xóa không
    if len(S) < N:
        print("Lỗi: Số lượng chữ số còn lại sau khi lọc (" + str(len(S)) + " số) không đủ để xóa " + str(N) + " ký tự!")
    else:
        print("Chuỗi số sau khi lọc sạch ký tự chữ là:", S)
        
        # THUẬT TOÁN TÌM SỐ LỚN NHẤT
        ket_qua = []

        for chu_so in S:
            # Vòng lặp so sánh và xóa các số nhỏ hơn ở phía trước
            while len(ket_qua) > 0 and N > 0 and chu_so > ket_qua[len(ket_qua) - 1]:
                ket_qua.pop()
                N = N - 1
            ket_qua.append(chu_so)

        # Nếu duyệt xong vẫn còn lượt xóa thì xóa tiếp ở cuối
        while N > 0:
            ket_qua.pop()
            N = N - 1

        # Ghép lại thành chuỗi kết quả
        so_lon_nhat = "".join(ket_qua)
        
        if so_lon_nhat == "":
            print("Số có giá trị lớn nhất sau khi xóa là: 0 (Đã xóa hết sạch số)")
        else:
            print("Số có giá trị lớn nhất sau khi xóa là:", so_lon_nhat)