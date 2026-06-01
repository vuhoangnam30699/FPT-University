import re

""" 4. Nhập vào một chuỗi từ người dùng, kiểm tra xem đó có phải địa chỉ email hợp lệ hay không? """

def kiem_tra_email(email):
    # Regex kiểm tra email
    cau_truc_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # So khớp chuỗi nhập vào với cấu trúc regex
    if re.match(cau_truc_email, email):
        return True
    return False

# Nhập email
chuoi_nhap = input("Nhập vào chuỗi cần kiểm tra email: ").strip()

# Kiểm tra
if kiem_tra_email(chuoi_nhap):
    print(f"'{chuoi_nhap}' là một địa chỉ email hợp lệ.")
else:
    print(f"'{chuoi_nhap}' không phải là một địa chỉ email hợp lệ.")