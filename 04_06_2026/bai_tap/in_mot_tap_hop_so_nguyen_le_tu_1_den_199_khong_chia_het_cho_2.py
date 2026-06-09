"""

Tạo một tập hợp gồm các số nguyên lẻ trong khoảng từ 1 đến 199, in chúng ra màn hình

"""


a = { x for x in range(1, 200) if x % 2 != 0 }
# a = set(range(1, 200, 2))
print(a)