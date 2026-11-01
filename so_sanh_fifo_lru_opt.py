# ============================================================
#  SO SÁNH THỰC NGHIỆM 3 THUẬT TOÁN THAY THẾ TRANG
#  FIFO - LRU - Optimal trên CÙNG MỘT chuỗi tham chiếu
#  Chạy: python so_sanh_thuc_nghiem.py
#  (Đồ thị cần: pip install matplotlib — không có thì vẫn in bảng)
# ============================================================
import random

# ---------- Cấu hình thí nghiệm ----------
SO_LAN_TRUY_CAP = 500        # số lượng mẫu (độ dài chuỗi tham chiếu)
SO_TRANG = 20                # trang được đánh số 0..19
SEED = 42                    # cố định seed để ai chạy cũng ra cùng kết quả
DS_KHUNG = list(range(10, 0, -1))   # số khung: 10, 9, ..., 1
MA = 100                     # thời gian truy cập RAM (ns)
THOI_GIAN_LOI = 8_000_000    # thời gian xử lý 1 lỗi trang (ns) = 8 ms


# ---------- Chuỗi tham chiếu có tính cục bộ (giống hàm của N1) ----------
def tao_chuoi(n=SO_LAN_TRUY_CAP, so_trang=SO_TRANG, seed=SEED):
    random.seed(seed)
    chuoi = []
    while len(chuoi) < n:
        bat_dau = random.randint(0, so_trang - 5)      # mỗi giai đoạn dùng 5 trang gần nhau
        vung = list(range(bat_dau, bat_dau + 5))
        for _ in range(50):
            chuoi.append(random.choice(vung))
    return chuoi[:n]


# ---------- 3 thuật toán: cùng đầu vào, trả về số lỗi trang ----------
def fifo(chuoi, so_khung):
    khung, loi = [], 0
    for p in chuoi:
        if p not in khung:
            loi += 1
            if len(khung) == so_khung:
                khung.pop(0)                 # bỏ trang vào sớm nhất
            khung.append(p)
    return loi


def lru(chuoi, so_khung):
    khung, loi = [], 0                       # đầu list = trang lâu nhất chưa dùng
    for p in chuoi:
        if p in khung:
            khung.remove(p)
        else:
            loi += 1
            if len(khung) == so_khung:
                khung.pop(0)
        khung.append(p)                      # trang vừa dùng đưa xuống cuối
    return loi


def optimal(chuoi, so_khung):
    khung, loi = [], 0
    for i, p in enumerate(chuoi):
        if p in khung:
            continue
        loi += 1
        if len(khung) < so_khung:
            khung.append(p)
        else:
            tuong_lai = chuoi[i + 1:]

            def lan_dung_tiep(q):
                return tuong_lai.index(q) if q in tuong_lai else float("inf")

            bo = max(khung, key=lan_dung_tiep)   # trang dùng lại xa nhất
            khung[khung.index(bo)] = p
    return loi


def eat_ms(so_loi, n):
    p = so_loi / n
    return ((1 - p) * MA + p * THOI_GIAN_LOI) / 1_000_000   # đổi ns -> ms


# ---------- Chạy thí nghiệm ----------
def main():
    chuoi = tao_chuoi()
    thuat_toan = {"FIFO": fifo, "LRU": lru, "Optimal": optimal}
    n = len(chuoi)

    print("=" * 66)
    print(" SO SÁNH THỰC NGHIỆM FIFO - LRU - OPTIMAL")
    print(f" Cùng 1 chuỗi: {n} lần truy cập, {len(set(chuoi))} trang khác nhau xuất hiện, seed = {SEED}")
    print(f" 30 truy cập đầu: {chuoi[:30]}")
    print("=" * 66)

    ket_qua = {ten: [] for ten in thuat_toan}
    print(f"\n{'Khung':>5} | {'FIFO':>6} | {'LRU':>6} | {'Optimal':>7} | {'FIFO vs LRU: ít lỗi hơn':<22}")
    print("-" * 58)
    for k in DS_KHUNG:
        loi = {ten: ham(chuoi, k) for ten, ham in thuat_toan.items()}
        for ten in thuat_toan:
            ket_qua[ten].append(loi[ten])
        # chỉ so giữa FIFO và LRU, vì Optimal không cài được trong thực tế
        if loi["FIFO"] < loi["LRU"]:
            thang = "FIFO"
        elif loi["LRU"] < loi["FIFO"]:
            thang = "LRU"
        else:
            thang = "Bằng nhau"
        print(f"{k:>5} | {loi['FIFO']:>6} | {loi['LRU']:>6} | {loi['Optimal']:>7} | {thang:<22}")

    print("\n(Số trong bảng = số lần lỗi trang trên tổng", n, "lần truy cập)")

    # Thời gian truy cập hiệu dụng
    print(f"\n{'Khung':>5} | {'EAT FIFO (ms)':>13} | {'EAT LRU (ms)':>12} | {'EAT Optimal (ms)':>16}")
    print("-" * 56)
    for i, k in enumerate(DS_KHUNG):
        print(f"{k:>5} | {eat_ms(ket_qua['FIFO'][i], n):>13.3f} | {eat_ms(ket_qua['LRU'][i], n):>12.3f} | "
              f"{eat_ms(ket_qua['Optimal'][i], n):>16.3f}")

    # Điểm thrashing: bước giảm 1 khung làm số lỗi LRU tăng mạnh nhất
    ds_lru = ket_qua["LRU"]
    buoc = max(range(1, len(DS_KHUNG)), key=lambda i: ds_lru[i] / ds_lru[i - 1])
    print(f"\nĐiểm Thrashing (LRU tăng mạnh nhất): {DS_KHUNG[buoc - 1]} -> {DS_KHUNG[buoc]} khung, "
          f"số lỗi {ds_lru[buoc - 1]} -> {ds_lru[buoc]} (gấp {ds_lru[buoc] / ds_lru[buoc - 1]:.1f} lần)")

    # Đồ thị
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("\nChưa cài matplotlib nên bỏ qua đồ thị (pip install matplotlib).")
        return
    for ten, ds in ket_qua.items():
        plt.plot(DS_KHUNG, ds, marker="o", label=ten)
    plt.axvline(5, color="red", linestyle="--", label="Kích thước vùng cục bộ = 5")
    plt.gca().invert_xaxis()
    plt.xlabel("Số khung trang (giảm dần)")
    plt.ylabel(f"Số lần lỗi trang (trên {n} lần truy cập)")
    plt.title("So sánh FIFO - LRU - Optimal trên cùng một chuỗi tham chiếu")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("so_sanh_thuc_nghiem.png", dpi=150)
    print("\nĐã lưu đồ thị: so_sanh_thuc_nghiem.png")
    plt.show()


if __name__ == "__main__":
    main()