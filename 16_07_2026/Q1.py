"""

Viết chương trình Python cho phép người dùng chọn 1 trong 3 chức năng sau:
1. Tính tổng chuỗi số
•	Nhập vào số nguyên n
•	Tính tổng:
S=1+11+111+… (n số hạng)
Enter a number: 5
OUTPUT
12345
2. In tam giác chữ cái
•	Nhập số dòng n
•	In ra tam giác chữ cái đối xứng
Ví dụ (n = 5)
A
ABA
ABCBA
ABCDCBA
ABCDEDCBA
3. Nén chuỗi (String Compression)
•	Nhập một chuỗi gồm các ký tự liên tiếp
•	In ra chuỗi nén theo dạng: ký tự + số lần lặp
Ví dụ
Input: pppppppppffffffffppppppp
Output: p9f8p7

"""



def tinh_tong_chuoi_so(n):
    tong = 0
    so_hang = 0
    for _ in range(n):
        so_hang = so_hang * 10 + 1
        tong += so_hang
    return tong


def in_tam_giac_chu_cai(n):
    for i in range(n):
        chuoi = ''.join(chr(ord('A') + j) for j in range(i + 1))
        print(chuoi + chuoi[-2::-1])


def nen_chuoi(s):
    ket_qua = []
    dem = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            dem += 1
        else:
            ket_qua.append(s[i - 1] + str(dem))
            dem = 1
    ket_qua.append(s[-1] + str(dem))
    return ''.join(ket_qua)


while True:
    print("\nChon chuc nang:")
    print("1. Tinh tong chuoi so")
    print("2. In tam giac chu cai")
    print("3. Nen chuoi")
    print("0. Thoat")

    chon = input("Nhap lua chon: ").strip()

    if chon == '1':
        n = int(input("Enter a number: "))
        print("OUTPUT")
        print(tinh_tong_chuoi_so(n))
    elif chon == '2':
        n = int(input("n = "))
        print("OUTPUT")
        in_tam_giac_chu_cai(n)
    elif chon == '3':
        s = input("Input: ")
        print("Output:", nen_chuoi(s))
    elif chon == '0':
        print("Bye bye!")
        break
    else:
        print("Lua chon khong hop le.")

