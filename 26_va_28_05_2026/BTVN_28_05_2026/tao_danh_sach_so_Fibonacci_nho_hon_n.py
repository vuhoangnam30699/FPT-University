""" 6.

Hãy nhập số nguyên n, tạo một list gồm các số fibonacci nhỏ hơn n và in ra
· Dãy fibonacci là dãy số nguyên được định nghĩa một cách đệ quy như sau: f(0)=0, f(1) = 1, f(1<n)=f(n-1)+f(n-2)

"""


def tao_list_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    # Khởi tạo list với 2 số đầu tiên của dãy
    fibo_list = [0, 1]
    
    while True:
        # Tính số tiếp theo bằng tổng 2 số cuối cùng trong list
        so_tiep_theo = fibo_list[-1] + fibo_list[-2]
        
        # Nếu số tiếp theo lớn hơn hoặc bằng n thì dừng lại
        if so_tiep_theo >= n:
            break
            
        fibo_list.append(so_tiep_theo)
        
    return fibo_list

try:
    n = int(input("Nhập số nguyên n: "))
    ket_qua = tao_list_fibonacci(n)
    print(f"Các số Fibonacci nhỏ hơn {n} là: {ket_qua}")
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ!")