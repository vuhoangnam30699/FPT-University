ho_ten = input("Nhập họ và tên đầy đủ: ")

# Loại bỏ khoảng trắng thừa ở đầu/cuối và tách thành danh sách các từ
cac_tu = ho_ten.strip().split()

# Kiểm tra nếu người dùng nhập ít nhất là 2 từ (đủ cả họ và tên)
if len(cac_tu) >= 2:
    # Lấy từ đầu tiên làm Họ
    ho = cac_tu[0]
    
    # Lấy từ cuối cùng làm Tên riêng
    vi_tri_cuoi_cung = len(cac_tu) - 1
    ten = cac_tu[vi_tri_cuoi_cung]
    
    print("Họ:", ho)
    print("Tên riêng:", ten)
else:
    print("Vui lòng nhập đầy đủ cả họ và tên (ít nhất 2 từ)!")