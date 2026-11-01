import random
import matplotlib.pyplot as plt
 
# ---------- N1: Tạo chuỗi tham chiếu (500 lần truy cập, 20 trang khác nhau) ----------
def tao_chuoi(n=500, so_trang=20, seed=42):
    random.seed(seed)
    chuoi = []
    while len(chuoi) < n:
        # Nguyên lý cục bộ: mỗi giai đoạn (50 lần truy cập) chỉ dùng 5 trang gần nhau
        bat_dau = random.randint(0, so_trang - 5)
        vung = list(range(bat_dau, bat_dau + 5))
        for _ in range(50):
            chuoi.append(random.choice(vung))
    return chuoi
 
# ---------- N3: FIFO ----------
def fifo(chuoi, so_khung):
    khung, loi = [], 0
    for p in chuoi:
        if p not in khung:
            loi += 1
            if len(khung) == so_khung:
                khung.pop(0)          # bỏ trang vào sớm nhất
            khung.append(p)
    return loi
 
# ---------- N4: LRU ----------
def lru(chuoi, so_khung):
    khung, loi = [], 0                # đầu list = trang lâu nhất chưa dùng
    for p in chuoi:
        if p in khung:
            khung.remove(p)           # dùng lại thì đưa xuống cuối
        else:
            loi += 1
            if len(khung) == so_khung:
                khung.pop(0)
        khung.append(p)
    return loi
 
# ---------- N5: Optimal ----------
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
            # chọn trang sẽ được dùng xa nhất trong tương lai (hoặc không dùng nữa)
            def lan_dung_tiep(q):
                return tuong_lai.index(q) if q in tuong_lai else float("inf")
            bo = max(khung, key=lan_dung_tiep)
            khung[khung.index(bo)] = p
    return loi
 
# ---------- N3: Thời gian truy cập hiệu dụng (ns) ----------
def eat(ti_le_loi, ma=100, thoi_gian_loi=8_000_000):
    return (1 - ti_le_loi) * ma + ti_le_loi * thoi_gian_loi
 
# ---------- N2 + N5: Thí nghiệm, bảng so sánh, đồ thị ----------
chuoi = tao_chuoi()
ds_khung = list(range(10, 0, -1))     # cắt giảm khung: 10, 9, ..., 1
thuat_toan = {"FIFO": fifo, "LRU": lru, "Optimal": optimal}
ket_qua = {ten: [] for ten in thuat_toan}

# --- PHẦN HÀM IN TERMINAL ĐƯỢC LÀM MỚI DỄ NHÌN ---
print("=" * 85)
print(f"{'Khung':^6} | {'Tỷ lệ lỗi trang (%)':^27} | {'Thời gian EAT (ms)':^36}")
print(f"{'':^6} | {'FIFO':^8} {'LRU':^8} {'Optimal':^9} | {'FIFO':^11} {'LRU':^11} {'Optimal':^11}")
print("=" * 85)

for k in ds_khung:
    ty_le = {}
    eat_val = {}
    for ten, ham in thuat_toan.items():
        t_le = ham(chuoi, k) / len(chuoi) * 100
        ty_le[ten] = t_le
        ket_qua[ten].append(t_le)
        # Tính EAT và đổi sang milisecond (ms) cho dễ đọc
        eat_val[ten] = eat(t_le / 100) / 1_000_000
    
    # Đánh dấu dòng bắt đầu xảy ra Thrashing (Khung < 5)
    canh_bao = " <-- THRASHING!" if k < 5 else ""
    
    print(f"{k:^6} | {ty_le['FIFO']:>6.1f}% {ty_le['LRU']:>6.1f}% {ty_le['Optimal']:>7.1f}% | "
          f"{eat_val['FIFO']:>9.2f} ms {eat_val['LRU']:>9.2f} ms {eat_val['Optimal']:>9.2f} ms{canh_bao}")

print("=" * 85)

# ---------- Đồ thị ----------
for ten, ds in ket_qua.items():
    plt.plot(ds_khung, ds, marker="o", label=ten)
plt.axvline(5, color="red", linestyle="--", label="Kích thước vùng cục bộ = 5")
plt.gca().invert_xaxis()              # số khung giảm dần từ trái sang phải
plt.xlabel("Số khung trang (giảm dần)")
plt.ylabel("Tỷ lệ lỗi trang (%)")
plt.title("Tỷ lệ lỗi trang khi cắt giảm khung - Thrashing")
plt.legend()
plt.grid(True)
plt.show()