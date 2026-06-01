input_string = input("Nhập dãy số (cách nhau bởi dấu cách hoặc tab): ")

# Tách chuỗi lớn thành một danh sách các chuỗi số nhỏ
danh_sach_chuoi_vua_nhap = input_string.split()

# Tạo một danh sách rỗng để chứa các số sau khi chuyển đổi
danh_sach_so_sau_chuyen_doi = []

# Duyệt qua từng chuỗi số trong danh sách để chuyển thành kiểu số
for x in danh_sach_chuoi_vua_nhap:
    # Nếu trong chuỗi có dấu chấm, đó là số thực (float)
    if "." in x:
        so = float(x)
    else:
        # Ngược lại là số nguyên (int)
        so = int(x)
    
    # Thêm số vừa chuyển đổi vào danh sách kết quả
    danh_sach_so_sau_chuyen_doi.append(so)

print("Dãy số vừa nhập là:", danh_sach_so_sau_chuyen_doi)