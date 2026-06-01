''' Ví dụ về phép nối chuỗi '''

a = 'Hello'
b = 'World'
print(a+b)						# 'Hello World'
c = 'Hello' 'Kitty'
print(c)						# 'HelloKitty'
d = '1'
'2'
'3'
print(d)						# '1'
e = ('1'
        '2'
     '3')
print(e)						# '123'
print(d + '23')					# '123'
#print(e '23')					# Lỗi

print('abc' * 3)				# 'abcabcabc'
print(5 * '10')					# '1010101010'
print('ab' + 'cd' * 3)			# 'abcdcdcd'

print('bcd' in 'abcdef')		# True
print('bcd' in 'abc' * 3)		# False
print('abc' not in 'ab' + 'cd')	# False



''' Cắt chuỗi '''

s = '0123456789'

print(s[3:6])				# 345
print(s[3:])				# 3456789
print(s[:6])				# 012345
print(s[-7:-4])				# 345
print(s[-4:-7])				# 
print(s[-4:-7:-1])			# 654
print(s[:len(s)])			# 0123456789
print(s[:len(s)-1])			# 012345678
print(s[:])					# 0123456789
print(s[len(s)::-1])		# 9876543210
print(s[len(s)-1::-1])		# 9876543210
print(s[len(s)-2::-1])		# 876543210




''' Định dạng chuỗi '''

print("Chao %s, gio la %d gio" % ('txnam', 10))			# Chao txnam, gio la 10 gio
print("Can bac 2 cua 2 = %f" % (2**0.5))				# Can bac 2 cua 2 = 1.414214
print("Can bac 2 cua 2 = %10.3f" % (2**0.5))			# Can bac 2 cua 2 =      1.414
print("Can bac 2 cua 2 = %10f" % (2**0.5))				# Can bac 2 cua 2 =   1.414214
print("Can bac 2 cua 2 = %.7f" % (2**0.5))				# Can bac 2 cua 2 = 1.4142136


''' Python cho phép định dạng chuỗi ở dạng f-string '''

myName = 'FPTU'
s = f'This is {myName}.'		# 'This is FPTU.'
w = f'{s} {myName}'				# 'This is FPTU. FPTU'
z = f'{{s}} {s}'				# '{s} This is FPTU.'

print(s)
print(w)
print(z)

''' Mạnh mẽ nhất là định dạng bằng format '''

# điền lần lượt từng giá trị vào giữa cặp ngoặc nhọn
print('a: {}, b: {}, c: {}'.format(1, 2, 3))

# điền nhưng không lần lượt
print('a: {1}, b: {2}, c: {0}'.format('one', 'two', 'three'))
print('two same values: {0}, {0}'.format (1, 2))

# điền và chỉ định từng giá trị
print('1: {one}, 2: {two}'.format(one = 111, two = 222))


''' Định dạng bằng format cho phép căn lề phong phú '''

# căn giữa: '	aaaa	'
print('{:^10}'.format('aaaa'))

# căn lề trái: 'aaaa	'
print('{:<10}'.format('aaaa'))

# căn lề phải: '	aaaa'
print('{:>10}'.format('aaaa'))

# Căn giữa, lấp đầy bằng dấu gạch ngang '-'
print('{:-^10}'.format('aaaa'))		# Kết quả: '---aaaa---'

# Căn trái, lấp đầy bằng dấu sao '*'
print('{:*<10}'.format('aaaa'))		# Kết quả: 'aaaa******'

# Căn phải, lấp đầy bằng dấu chấm '.'
print('{:.>10}'.format('aaaa'))		# Kết quả: '......aaaa'



"""

capitalize()		# Viết hoa chữ đầu, còn lại thường
upper()				# chuyển hết thành chữ hoa
lower()				# chuyển hết thành chữ thường
swapcase()			# chữ thường thành hoa và ngược lại
title()				# chữ đầu của mỗi từ viết hoa, còn lại viết thường

"""


''' Các phương thúc căn lề

center(width[, fillchar]): Căn giữa
ljust(width[, fillchar]): Căn trái
rjust(width[, fillchar]): Căn phải

'''



''' Các phương thức cắt chuỗi phần dư

strip([chars]): loại bỏ những ký tự đầu hoặc cuối chuỗi thuộc vào danh sách [chars], hoặc ký tự trống
rstrip([chars]): như strip nhưng cho bên phải
lstrip([chars]): như strip nhưng cho bên trái

'''


''' Tách chuỗi
split(sep, maxsplit): tách chuỗi thành 1 danh sách, sử dụng dấu ngăn cách sep, thực hiện tối đa maxsplit lần
rsplit(sep, maxsplit): thực hiện như split nhưng theo hướng ngược từ phía cuối chuỗi

'''


''' Các phương thức khác

· join(list): ghép các phần tử trong list bởi phần gạch nối là nội
dung của chuỗi, ví dụ: '-'.join(('1', '2', '3'))
· replace(old, new [,count]): thế nội dung old bằng nội dung new,
tối đa count lần

· count(sub, [start, [end]]): đếm số lần xuất hiện của sub
· startswith(prefix): kiểm tra đầu có là prefix không
· endswith(prefix): kiểm tra cuối có là prefix không
· find(sub[, start[, end]]): tìm vị trí của sub (-1: không có)
· rfind(sub[, start[, end]]): như find nhưng tìm từ cuối
· islower(), isupper(), istitle(), isdigit(), isspace(), isalpha(),
isnumeric()
· index(sub) giống find, nhưng sinh ngoại lệ nếu không tìm thấy

'''

'''
    
Các hàm dựng sẵn hỗ trợ chuyển đổi
· Hàm chr(n): chuyển đổi giá trị số sang mã unicode
· Hàm ord(c): chuyển đổi kí tự unicode sang giá trị số
· Hàm len(s): trả về độ dài (số kí tự) của chuỗi
· Hàm str(v): chuyển đổi giá trị của biến v sang thể hiện ở dạng chuỗi

'''

s = '€'					# s chứa kí tự euro có mã 8364
print(ord(s))   		# in ra mã của s (8364)
print(chr(8364))		# in ra kí tự ứng với mã 8364
n = 3+4j				# n là số phức 3+4i
print(n)				# tự động chuyển n sang chuỗi và in ra
#print(len(n))			# LỖI
print(len(str(n)))		# in ra độ dài của n dạng chuỗi



# 28/05/2026


'''

Bất biến (immutable): ko thay đổi: bool, int, float, str, tuple, frozenset
Khả biến (mutable): list, set, dict

* vẫn có thể thay đổi giá trị của int nhưng tại sao nói "bất biến"
-> Python ko thực sự thay đổi giá trị của int, phần mềm tạo vùng nhớ chứa giá trị mới và cho biến "trỏ" tới vùng đó

'''

'''

Giới thiệu và khai báo

List = dãy các đối tượng (1 loại array đa năng)

Các phần tử con trong list ko nhất thiết phải cùng kiểu dữ liệu

Khai báo trực tiếp: liệt kê các phần tử con đặt trong cặp ngoặc vuông ([]), ngăn cách bởi dấu phẩy (,)

Kiểu chuỗi (str) trong Python có thể xem như một list đặc biệt chứa các ký tự và không thể thay đổi (immutable)

'''


'''

Khởi tạo list


Tạo list bằng constructor (hàm tạo)
l1 = list([1,2,3,4])		# list 4 số nguyên
l2 = list('abc')			# list 3 chuỗi con
l3 = list()					# list rỗng


Tạo list bằng list comprehension (bộ suy diễn danh sách)
một đoạn mã ngắn trả về các phần tử thuộc list

# list 1000 số nguyên từ 0 đến 999
X = [n for n in range(1000)]

# list gồm 10 list con là các cặp [x, x^2]
# với x chạy từ 0 đến 9
Y = [[x, x*x] for x in range(10)]

'''




""" So sánh 2 list: theo thứ tự từ điển (như str) """

a = [1, 2,3]
b = [1, 2, 3, 4]
c = [1.5]
d = ['a', 'b', 'c']
print(a > b)						# False
print(a == b)						# False
print(a < b)						# True
print(a + [4] == b)					# True
print(c <= b)						# False
print(d != a)						# True
print(d == list('abc'))				# True
#print(d >= c)						# Lỗi


""" Phép toán, chỉ mục và cắt

Giữa list và str có sự tương đồng nhất định

-> List cũng hỗ trợ 3 phép toán: ghép nối (+), nhân bản (*) và kiểm tra nội dung (in)
-> List sử dụng hệ thống chỉ mục và các phép cắt phần con tương tự như str

Điểm khác biệt: nội dung của list có thể thay đổi

"""

# khởi tạo list ban đầu
l1 = list([1, 2, 3, 4])
# thay đổi giá trị của phần tử cuối cùng
l1[-1] = list('abc')
# in nội dung list: [1, 2, 3, ['a', 'b', 'c']]
print(l1)


""" Chỉ mục, lát cắt, xóa dữ liệu với list """

a = list('abcde')
print(a)				# ['a', 'b', 'c', 'd', 'e']
a[-1] =[0,5,9]			# thay đổi phần tử cuối cùng
print(a)				# ['a', 'b', 'c', 'd', [0, 5, 9]]
a[1:3] = [1, 2, 3]		# thay đổi một đoạn
print(a)				# ['a', 1, 2, 3, 'd', [0, 5, 9]]
print(a[2 ::- 1])		# [2, 1, 'a']
#a[2 ::- 1] = [0]		# lỗi, đoạn ngược không thể thay đổi
del a[2 ::- 1]			# xóa đoạn con từ 2 trở về đầu
print(a)				# [3, 'd', [0, 5,9]]
del a					# xóa biến a
#print(a)				# lỗi, a không tồn tại



""" Các phương thức của list

Một số phương thức thường hay sử dụng

· count(sub, [start, [end]]): đếm số lần xuất hiện của sub
· index(sub[, start[, end]]): tìm vị trí xuất hiện của sub, phát sinh lỗi ValueError nếu không tìm thấy
· clear(): xóa trắng list
· append(x): thêm x vào cuối list
· extend(x): thêm các phần tử của x vào cuối list
· insert (p, x): chèn x vào vị trí p trong list
· pop(p): bỏ phần tử thứ p ra khỏi list (trả về giá trị của phần tử đó), nếu không chỉ định p thì lấy phần tử cuối
· copy(): tạo bản sao của list (tương tự list[:])
· remove(x): bỏ phần tử đầu tiên trong list có giá trị x, báo lỗi ValueError nếu không tìm thấy
· reverse(): đảo ngược các phần tử trong list
· sort(key=None, reverse=False): mặc định là sắp xếp các phần tử từ bé đến lớn trong list bằng cách so sánh trực tiếp giá trị

"""

x = "Trương Xuân Nam". split()
x.sort(key=str.lower)
print(x)						# ['Nam', 'Trương', 'Xuân']


""" Ví dụ về sắp xếp với list """

a =['123', '13', '90', "-1", -100]
#a.sort()									# lỗi, vì các phần tử không cùng kiểu
a[-1] = '-100'								# thay đổi phần tử cuối thành dạng chuỗi
a.sort()									# xếp tăng dần theo so sánh chuỗi
print(a)									# ['-1', '-100', '123', '13', '90']
a.sort(key=int)								# chuyển thành số nguyên rồi sắp xếp
print(a)									# ['-100', '-1', '13', '90', '123']
a.sort(key=int, reverse=True)
print(a)									# ['123', '90', '13', '-1', '-100']


""" Duyệt list với vòng lặp for """

my_list = ['foo', 'bar', 'baz', 'noo']

# duyệt các phần tử, cách làm đơn giản nhất
for item in my_list:
    print(item)
    
# duyệt các phần tử theo giá trị chỉ mục
for i in range(len(my_list)):
    print(i, my_list[i])
    
# duyệt theo giá trị chỉ mục nhưng nhanh hơn
# với cách sử dụng hàm enumerate
for i, item in enumerate(my_list):
    print(i, item)
    
    
""" Ví dụ về làm việc với list """

# tạo và in nội dung của một list
danhsach = ["apple", "banana", "cherry"]

for x in danhsach:
    print(x)
# thêm một phần tử vào cuối list và lại in ra
danhsach. append ("orange")
print(danhsach)
# thêm một phần tử vào giữa list và in ra
danhsach.insert(1, "orange")
print(danhsach)
# sắp xếp lại danh sách và in ra
danhsach.sort()
print(danhsach)
    
""" Một số thao tác thông dụng với list

1. Tạo một list
2. Duyệt list
3. Truy cập phần tử theo chỉ số
4. Thay đổi nội dung phần tử
5. Cắt list
6. Thêm phần tử vào list
7. Bỏ phần tử khỏi list
8. Tìm kiếm phần tử trong list
9. Sắp xếp các phần tử trong list
10. List hỗn hợp

"""


""" Các cách khai báo tuple """

# Cách 1: Dùng cặp dấu ngoặc đơn
tup1 = ()

# Cách 2: Dùng hàm khởi tạo tuple()
tup2 = tuple()

# Tuple chứa các phần tử cùng kiểu dữ liệu
điem_so = (9.5, 8.0, 7.5)

# Tuple chứa nhiều kiểu dữ liệu khác nhau (String, Int, Float, Boolean)
user_info = ("Nam", 20, 65.5, True)

# SAI: Python hiểu đây là kiểu số nguyên (int)
khong_phai_tuple = (5)  

# ĐÚNG: Phải có dấu phẩy ở cuối
la_tuple = (5,)

# Python tự hiểu đây là một tuple
toa_do = 10, 20, 30  

print(type(toa_do)) # Kết quả: <class 'tuple'>

# Chuyển từ List sang Tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list) # Kết quả: (1, 2, 3)

# Chuyển từ String sang Tuple (mỗi ký tự là một phần tử)
chuoi = "ABC"
tup_chuoi = tuple(chuoi) # Kết quả: ('A', 'B', 'C')


# Khai báo Tuple lồng nhau (Nested Tuple)
matrix = ((1, 2), (3, 4), (5, 6))


""" Tuple và list nhiều điểm giống nhau

· Tuple có thể tạo bằng constructor hoặc generator (bộ sinh) - một cách viết tương tự list comprehension
· Tuple hỗ trợ 3 phép toán: +, *, in
· Tuple cho phép sử dụng chỉ mục và cắt
· Các phương thức thường dùng của tuple
    · count(v): đếm số lần xuất hiện của v trong tuple
    · index(sub[, start[, end]]): tương tự như str và list
· Tuple khác list ở điểm nào?
    · Chiếm ít bộ nhớ hơn
    · Nhanh hơn

"""


""" Bộ sinh của tuple chỉ dùng được 1 lần """

# t0 viết giống như bộ suy diễn danh sách
t0 = (c for c in 'Hello!')
# tạo t1 từ t0
t1 = tuple(t0)
# tạo t2 từ t0
t2 = tuple(t0)
print(t0)# <generator object <genexpr> at XXXX>
print(t1)		# ('H', 'e', '1', '1', 'o', '!')
print(t2)		# () <~~ như vậy t0 chỉ dùng được một lần


""" Tính bất biến của kiểu tuple """

a = (1, 2, [3,4], 'abc')
print(a[2])						# [3,4]
a[2].append('xyz')				# a[2] trở thành [3, 4, 'xyz']
print(a)						# (1, 2, [3, 4, 'xyz'], 'abc')
a[2] = '123'					# lỗi
a = (1, 2, 3)					# ok: thay đổi a thành tuple mới
a += (4, 5)						# ok: a thay đổi thành tuple mới
print(a)						# (1, 2, 3, 4, 5)
del a							# ok: xóa hoàn toàn a

""" Hàm dựng săn làm việc với list và tuple
· Hàm all(X): trả về True nếu tất cả các phần tử của X đều là True hoặc tương đương với True hoặc x rỗng
· Hàm any(X): trả về True nếu có ít nhất một phần tử của X là True hoặc tương đương với True
· Hàm len(X): trả về số lượng phần tử của X
· Hàm list(X): tạo một list gồm các phần tử con của X
· Hàm max(X): trả về giá trị lớn nhất trong X
· Hàm min(X): trả về giá trị nhỏ nhất trong X
· Hàm sorted(X): trả về danh sách mới gồm các phần tử của X đã được sắp xếp
· Hàm sum(X): trả về tổng các phần tử trong X

"""



""" Range là một tuple đặc biệt?
· Chúng ta đã làm quen với range khi dùng vòng for
· range(stop): tạo miền từ 0 đến stop-1
· range(start, stop[, step]): tạo miền từ start đến stop-1, với bước nhảy là step
· Nếu không chỉ định thì step = 1
· Nếu step là số âm sẽ tạo miền đếm giảm dần (start > stop)

- Vậy range khác gì một tuple đặc biệt
· Range chỉ chứa số nguyên
· Range nhanh hơn rất nhiều
· Range chiếm ít bộ nhớ hơn
· Range vẫn hỗ trợ chỉ mục và cắt (nhưng khá đặc biệt)
· Không nên coi Range là một Tuple !!!

"""










    
    




