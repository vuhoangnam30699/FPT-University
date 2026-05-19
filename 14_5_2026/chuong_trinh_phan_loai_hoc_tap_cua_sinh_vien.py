
dtb = float(input("Nhập điểm trung bình học tập của sinh viên: "))


if dtb < 3.5:
    xep_loai = "Yếu"
elif dtb < 5.0:
    xep_loai = "Kém"
elif dtb < 6.5:
    xep_loai = "Trung bình"
elif dtb < 8.0:
    xep_loai = "Khá"
elif dtb < 9.0:
    xep_loai = "Giỏi"
else:
    xep_loai = "Xuất sắc"

print(f"Xếp loại học tập: {xep_loai}")