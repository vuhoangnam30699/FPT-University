"""

Đọc 1 file, thống kê và in ra tất cả các chữ cái có trong
file và số lần xuất hiện của các chữ đó

"""


dem_chu_cai = {}

try:
    with open("test.txt", 'r', encoding='utf-8') as file:
        for dong in file:
            dong_chu_thuong = dong.lower()
                
            for ky_tu in dong_chu_thuong:
                if ky_tu.isalnum():
                    if ky_tu in dem_chu_cai:
                        dem_chu_cai[ky_tu] += 1
                    else:
                        dem_chu_cai[ky_tu] = 1

    if dem_chu_cai:
        for chu_cai in sorted(dem_chu_cai.keys()):
            print(f"Chữ cái '{chu_cai}' xuất hiện: {dem_chu_cai[chu_cai]} lần")
    else:
            print("File trống hoặc không chứa chữ cái nào.")

except FileNotFoundError:
    print("Lỗi: Không tìm thấy file.")