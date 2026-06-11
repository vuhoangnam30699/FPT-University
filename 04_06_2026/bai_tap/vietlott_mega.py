N = int(input("Nhập số người chơi N: "))
danh_sach_nguoi_choi = []

# Nhập vé cho từng người
for i in range(N):
    # Nhập 6 số trên 1 dòng, cách nhau bằng khoảng trắng, sau đó chuyển thành set
    ve = set(map(int, input(f"Nhập 6 số của người thứ {i+1}: ").split()))
    danh_sach_nguoi_choi.append(ve)

# Nhập kết quả giải đặc biệt
giai_dac_biet = set(map(int, input("Nhập 6 số của giải đặc biệt: ").split()))

print("\n--- KẾT QUẢ ---")
nguoi_chien_thang = 0

# Kiểm tra từng vé
for i, ve in enumerate(danh_sach_nguoi_choi):
    # Tìm các số trùng khớp giữa vé của người chơi và giải đặc biệt
    so_trung = ve.intersection(giai_dac_biet)
    
    # Nếu trùng từ 5 số trở lên thì thắng
    if len(so_trung) >= 5:
        print(f"Người chơi thứ {i+1} THẮNG CỘC! Bộ số: {ve} (Trúng {len(so_trung)} số: {so_trung})")
        nguoi_chien_thang += 1

if nguoi_chien_thang == 0:
    print("Không có người chơi nào thắng cuộc ở vòng này.")