input_string = input("Nhập vào một dãy các từ: ")

# Tạo một danh sách rỗng để lưu các chữ cái đã kiểm tra (tránh in trùng)
chu_cai_da_dem = []

print("Thống kê số lần xuất hiện của các chữ cái:")

# Duyệt qua từng ký tự trong chuỗi ban đầu
for ky_tu in input_string:
    # Kiểm tra xem ký tự đó có phải là chữ cái không (bỏ qua khoảng trắng, dấu câu...)
    if ky_tu.isalpha() == True:
        # Nếu chữ cái này chưa từng được đếm trước đó
        if ky_tu not in chu_cai_da_dem:
            # Đếm số lần xuất hiện của chữ cái này trong chuỗi
            so_lan = input_string.count(ky_tu)
            
            print("Chữ '" + ky_tu + "' xuất hiện:", so_lan, "lần")
            
            # Thêm chữ cái này vào danh sách đã đếm
            chu_cai_da_dem.append(ky_tu)