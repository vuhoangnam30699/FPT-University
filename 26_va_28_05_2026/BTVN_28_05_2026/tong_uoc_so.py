import math

""" 3. Nhập số n, in ra các số nguyên dương nhỏ hơn n có tổng các ước số thực sự lớn hơn chính nó. """


def tinh_tong_uoc_thuc_su(x):
    if x <= 1:
        return 0
    
    tong = 1  # 1 luôn là ước thực sự của mọi số lớn hơn 1
    can_bac_hai = int(math.sqrt(x))
    
    for i in range(2, can_bac_hai + 1):
        if x % i == 0:
            tong += i
            # Nếu ước số đối diện khác i thì cộng vào luôn
            if i != x // i:
                tong += x // i
    return tong


try:
    n = int(input("Nhập số nguyên dương n: "))

    if n <= 0:
        print("Vui lòng nhập số nguyên dương lớn hơn 0.")
    else:
        # Mình đã xóa dòng chứa list_so_doi_dan ở đây rồi nhé!
        print(f"Các số nguyên dương nhỏ hơn {n} có tổng các ước thực sự lớn hơn chính nó là:")
        
        co_so_nao = False
        for k in range(1, n):
            if tinh_tong_uoc_thuc_su(k) > k:
                print(k, end=" ")
                co_so_nao = True
                
        if not co_so_nao:
            print("Không có số nào thỏa mãn.")
        print()  # Xuống dòng khi kết thúc

except ValueError:
    print("Vui lòng chỉ nhập số nguyên.")