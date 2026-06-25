"""

Đọc 1 file, thống kê và tần xuất xuất hiện của tất cả
các từ trong file, in theo thứ tự giảm dần của số lần
xuất hiện

"""


dem_tu = {}

try:
    with open("test.txt", 'r', encoding='utf-8') as file:
        for dong in file:
            
            dong_chu_thuong = dong.lower()
                
            
            dong_lam_sach = ""
            for ky_tu in dong_chu_thuong:
                if ky_tu.isalnum() or ky_tu.isspace():
                    
                    dong_lam_sach += ky_tu
                else:
                    
                    dong_lam_sach += " "
                
            
            cac_tu = dong_lam_sach.split()
                
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