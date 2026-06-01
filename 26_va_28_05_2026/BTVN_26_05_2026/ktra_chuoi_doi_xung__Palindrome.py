S_ban_dau = input("Nhập chuỗi S cần kiểm tra: ")

# Làm sạch chuỗi: Chuyển về chữ thường và xóa khoảng trắng
S = S_ban_dau.lower().replace(" ", "")

# Tạo một chuỗi rỗng để chứa chuỗi đảo ngược
S_dao_nguoc = ""

# Duyệt ngược từ cuối chuỗi về đầu chuỗi để tạo chuỗi đảo ngược
vi_tri_cuoi = len(S) - 1
for i in range(vi_tri_cuoi, -1, -1):
    S_dao_nguoc = S_dao_nguoc + S[i]

# So sánh chuỗi ban đầu và chuỗi đảo ngược
if S == S_dao_nguoc:
    print("Chuỗi S là dạng ĐỐI XỨNG!")
else:
    print("Chuỗi S KHÔNG PHẢI là dạng đối xứng!")