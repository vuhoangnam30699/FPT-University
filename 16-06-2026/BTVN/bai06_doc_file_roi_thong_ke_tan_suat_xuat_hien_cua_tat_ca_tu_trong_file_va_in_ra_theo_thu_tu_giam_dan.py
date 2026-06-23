"""

Đọc 1 file, thống kê và tần xuất xuất hiện của tất cả
các từ trong file, in theo thứ tự giảm dần của số lần
xuất hiện

"""


dem_tu = {}

try:
    with open("test.txt", 'r', encoding='utf-8') as file:
        for dong in file:
            # Chuyển toàn bộ dòng thành chữ thường
            dong_chu_thuong = dong.lower()
                
            # Thay thế tất cả dấu câu (ở đầu, cuối, hay ở giữa) thành khoảng trắng
            dong_lam_sach = ""
            for ky_tu in dong_chu_thuong:
                if ky_tu.isalnum() or ky_tu.isspace():
                    # Nếu là chữ, số hoặc khoảng trắng (cách, tab, xuống dòng) thì giữ lại
                    dong_lam_sach += ky_tu
                else:
                    # Nếu là dấu câu (/, -, ., !...) thì biến thành khoảng trắng
                    dong_lam_sach += " "
                
            # Tách dòng thành danh sách các từ
            cac_tu = dong_lam_sach.split()
                
            # Đếm tần suất bằng Dictionary
            for tu in cac_tu:
                if tu in dem_tu:
                    dem_tu[tu] += 1
                else:
                    dem_tu[tu] = 1

        if dem_tu:
            tu_da_sap_xep = sorted(dem_tu.items(), key=lambda item: item[1], reverse=True)
            for tu, so_lan in tu_da_sap_xep:
                print(f"Từ '{tu}': xuất hiện {so_lan} lần")
        else:
            print("File trống hoặc không có từ hợp lệ.")

except FileNotFoundError:
    print("Lỗi: Không tìm thấy file.")