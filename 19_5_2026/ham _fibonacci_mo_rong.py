"""

Hàm fibo mở rộng được định nghĩa như sau:

   fibo(0 <= n < k, k) = n
                            k
   fibo(n >= k, k)     =    ∑  fibo(n - i, k)
                           i=1

Viết chương trình nhập n và k sau đó tính fibo(n, k)


"""


def fibo_mo_rong(n, k):
    # Khởi tạo mảng lưu các giá trị fibo từ 0 đến n
    f = []
    
    # Trường hợp 0 <= n < k
    i = 0
    while i < k:
        f.append(i)
        i += 1
        
    # Nếu n nhỏ hơn k thì trả về kết quả luôn
    if n < k:
        return f[n]
        
    # Tính toán các giá trị từ k đến n bằng vòng lặp while
    current_n = k
    while current_n <= n:
        tong = 0
        step = 1
        # Tính tổng của k phần tử liền trước
        while step <= k:
            tong += f[current_n - step]
            step += 1
            
        f.append(tong)
        current_n += 1
        
    return f[n]


n = int(input("Nhập n: "))
k = int(input("Nhập k: "))

if k <= 0 or n < 0:
    print("Vui lòng nhập k > 0 và n >= 0!")
else:
    ket_qua = fibo_mo_rong(n, k)
    print(f"Giá trị fibo({n}, {k}) là: {ket_qua}")