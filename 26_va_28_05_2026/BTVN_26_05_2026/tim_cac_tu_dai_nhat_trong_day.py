input_string = input("Nhập vào một dãy các từ: ")

# Loại bỏ các dấu câu dính vào từ
chuoi_sach = ""
for ky_tu in input_string:
    # Nếu là chữ cái, chữ số hoặc khoảng trắng thì giữ lại
    if ky_tu.isalnum() == True or ky_tu == " ":
        chuoi_sach = chuoi_sach + ky_tu
    else:
        # Nếu là dấu câu (như , . ! ?), thay bằng khoảng trắng để không bị dính từ
        chuoi_sach = chuoi_sach + " "

# Tách chuỗi đã làm sạch thành danh sách các từ độc lập
cac_tu = chuoi_sach.split()

# Tìm độ dài lớn nhất của một từ
do_dai_lon_nhat = 0
for tu in cac_tu:
    do_dai_hien_tai = len(tu)
    if do_dai_hien_tai > do_dai_lon_nhat:
        do_dai_lon_nhat = do_dai_hien_tai

print("Các từ có độ dài lớn nhất (độ dài =", do_dai_lon_nhat, ") là:")

# In ra các từ có cùng độ dài lớn nhất
for tu in cac_tu:
    if len(tu) == do_dai_lon_nhat:
        print(tu)