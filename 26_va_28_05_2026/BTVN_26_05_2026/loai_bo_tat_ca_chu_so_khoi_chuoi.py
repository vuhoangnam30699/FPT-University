s = input("Nhập chuỗi chứa ký tự và chữ số: ")

# Tạo một chuỗi rỗng để tích lũy các ký tự chữ cái
chuoi_moi = ""

# Duyệt qua từng ký tự trong chuỗi ban đầu
for ky_tu in s:
    # Nếu ký tự KHÔNG phải là chữ số thì giữ lại
    if ky_tu.isdigit() == False:
        chuoi_moi = chuoi_moi + ky_tu

print("Chuỗi sau khi loại bỏ chữ số:", chuoi_moi)