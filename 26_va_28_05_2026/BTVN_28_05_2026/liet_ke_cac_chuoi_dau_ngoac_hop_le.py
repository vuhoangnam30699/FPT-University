""" 8.


Liệt kê các chuỗi độ dài ít hơn N của tuple X gồm các chuỗi được định nghĩa như sau:
-> Chuỗi M = *()' thuộc X
-> Nếu chuỗi A thuộc X thì chuỗi (A) cũng thuộc X
-> Nếu chuỗi A và B thuộc X thì chuỗi AB cũng thuộc X


"""


def sinh_chuoi_ngoac(n):
    ket_qua = []
    
    # Hàm backtrack để tìm các chuỗi hợp lệ
    def backtrack(chuoi_hien_tai, mo, dong, do_dai_toi_da):
        # Nếu chuỗi hiện tại có độ dài lớn hơn 0, nó là một chuỗi hợp lệ -> thêm vào list
        if len(chuoi_hien_tai) > 0:
            ket_qua.append(chuoi_hien_tai)
            
        # Thêm nhánh mở ngoặc '(' nếu tổng độ dài sau khi thêm vẫn < n
        # và số lượng dấu mở chưa vượt quá một nửa độ dài tối đa
        if len(chuoi_hien_tai) + 2 <= do_dai_toi_da and mo < do_dai_toi_da // 2:
            backtrack(chuoi_hien_tai + '(', mo + 1, dong, do_dai_toi_da)
            
        # Thêm nhánh đóng ngoặc ')' nếu số lượng dấu đóng ít hơn dấu mở
        if dong < mo:
            backtrack(chuoi_hien_tai + ')', mo, dong + 1, do_dai_toi_da)

    # Vì độ dài phải ÍT HƠN N, nên độ dài tối đa tối đa chỉ có thể là N - 1
    # Dấu ngoặc luôn đi theo cặp nên độ dài tối đa phải là số chẵn
    do_dai_toi_da = n - 1
    if do_dai_toi_da % 2 != 0:
        do_dai_toi_da -= 1
        
    if do_dai_toi_da >= 2:
        # Bắt đầu chạy từ chuỗi rỗng
        backtrack("", 0, 0, do_dai_toi_da)
        
    # Lọc lại để sắp xếp theo độ dài hoặc chuyển thành tuple X theo yêu cầu đề bài
    # (Đề bài yêu cầu tuple X gồm các chuỗi này)
    X = tuple(sorted(list(set(ket_qua)), key=len))
    return X

# Nhập N để chạy thử
try:
    N = int(input("Nhập số nguyên N (độ dài giới hạn): "))
    X = sinh_chuoi_ngoac(N)
    print(f"Tuple X gồm các chuỗi hợp lệ có độ dài < {N}:")
    for chuoi in X:
        print(f"Chuỗi: {chuoi:<10} (Độ dài: {len(chuoi)})")
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ!")