"""		Set

1. Giới thiệu

Tập hợp (set) là kiểu dữ liệu đặc sắc trong Python, lấy cảm hứng từ khái niệm tập hợp trong toán học
    · Các đối tượng con đôi một khác nhau: nếu đưa các đối tượng giống nhau vào tập hợp, Python sẽ chỉ giữ lại một
    · Không có tính thứ tự: không thể truy cập đến phần tử con thông qua hệ thống chỉ mục
    · Không phải dữ liệu nào cũng đưa được vào tập hợp: dữ liệu con bắt buộc phải là dạng bất biến (immutable)
    · Thêm: Python sử dụng cấu trúc dữ liệu bảng băm (hashtable) cho tập hợp, đây chính là lý do dữ liệu con phải bất biến để
            tránh việc dữ liệu bị thay đổi một cách bất lường
            
2. Khởi tạo

Tương tự như danh sách và hàng, khởi tạo tập hợp đơn giản nhất bằng cách liệt kê các phần tử con:
    · Đặt trong cặp ngoặc nhọn {}
    · Ngăn cách bởi phẩy
    · Chú ý: cách này không dùng để khởi tạo tập rỗng
    
    >>> basket = {'apple', 'orange', 'apple', 'pear'}
    >>> print(basket)			# xóa phần tử trùng nhau
    {'orange', 'pear', 'apple'}
    
Tạo tập hợp bằng hàm tạo hoặc các phép toán tập hợp

s1 = set([1, 2,3,4])		# {1, 2, 3, 4} - copy từ list
s2 = set((1,1,1))			# {1} - copy từ tuple, bỏ lặp
s3 = s1 - s2				# {2, 3, 4} - hiệu của hai tập
s4 = set(range(1,100))		# {1, 2, 3, ... , 98, 99}
s5 = set()					# {} - tập rỗng


Tập hợp cũng có thể khởi bằng bộ suy diễn tập hợp (set comprehension), cú pháp tương tự như danh sách


Dạng thông dụng nhất: lặp
    · { <biểu thức> for <biến> in <tuần tự> }
    " { x for x in 'abracadabra' }

Dạng phức tạp hơn: lặp và điều kiện
    · { <biểu thức> for <biến> in <tuần tự> if <điều kiện> }
    " { x for x in 'abracadabra' if x not in 'abc' }

Dạng phức tạp hơn nữa: lặp và điều kiện rẽ nhánh
    · Trường hợp này phải kết hợp lặp và phép toán if (không dùng rẽ nhánh if được)
    · { <A> if <điều kiện> else <B> for <biến> in <tuần tự> }
    " { '?' if x in 'abc' else x for x in 'abracadabra' }
    

Bộ suy diễn tập hợp đôi khi khá phức tạp
Ví dụ: tạo tập hợp chứa mọi hoán vị của chuỗi 'abc'

    s = {
        x + y + z
        for x in 'abc'
            for y in 'abc'
                for z in 'abc'
                    if x != y != z != x
        }

Set không thể chứa những đối tượng mutable (có thể bị thay đổi), mặc dù chính set lại có thể thay đổi
a = set(([1,2],[2,3]))		# lỗi
a = set(((1,2),(2,3)))		# {(1, 2), (2, 3)}
a. add ("abc")				# {(1,2), "abc", (2,3)}


3. Các phép toán trên set

    1. Phép giao (&)					: Lấy phần chung của hai tập
    2. Phép hợp (|)						: Lấy phần gộp của hai tập
    3. Phép hiệu (-)					: Lấy phần riêng của một tập
    4. Phép loại (^)					: Lấy phần khác (loại bỏ phần chung)
    5. Kiểm tra tồn tại (in)			: Trả về True nếu phần tử nằm trong tập hợp
    6. Kiểm tra không thuộc (not in)	: Trả về True nếu phần tử không thuộc tập hợp
    7. So sánh “bằng" (==)				: Trả về True nếu hai tập giống nhau
    8. So sánh “khác” (!=)				: Trả về True nếu có ít nhất một phần tử thuộc tập này mà không thuộc tập kia
    9. So sánh “lớn hơn” (>)			: Trả về True nếu mọi phần tử của tập thứ hai đều có trong tập thứ nhất và có ít nhất một
                                            phần tử thuộc tập thứ nhất không xuất hiện trong tập thứ hai                                         
    10. So sánh “lớn hơn hoặc bằng” (>=): Trả về True nếu tập thứ nhất bằng hoặc lớn hơn hoặc bằng” tập thứ hai
    11. So sánh “nhỏ hơn" (<)			: Trả về True nếu mọi phần tử thuộc tập thứ nhất đều có trong tập thứ hai và có ít nhất một phần
                                            tử thuộc tập thứ hai không xuất hiện trong tập thứ nhất                                         
    12. So sánh “nhỏ hơn hoặc bằng" (<=): Trả về True nếu tập thứ nhất bằng hoặc nhỏ hơn tập thứ hai
    

a = set('abracadabra')		# {'d', 'r', 'c', 'b', 'a'}
b = set('alacazam')			# {'z', 'c', 'm', '1', 'a'}

# Phép Hiệu: thuộc a nhưng không thuộc b
print(a - b)				# {'r', 'd', 'b'}

# Phép Hợp: thuộc a hoặc b
print(a | b)				# {'a', 'c', 'r', 'd', 'b', 'm', 'z', '1'}

# Phép Giao: thuộc cả a và b
print(a & b)				# {'a', 'c'}


# Phép Xor: thuộc hoặc a, hoặc b nhưng không
print(a ^ b)				# {'r', 'd', 'b', 'm', 'z', '1'}


4. Duyệt các phần tử của tập hợp

Cách đơn giản nhất là duyệt bằng vòng for
    a = { 10, 2,3,1,3,2,10 }
    for e in a:
        print(e)
Cẩn thận: thứ tự in kết quả của vòng for không nhất thiết phải theo thứ tự các phần tử đưa vào tập hợp

Trường hợp cần duyệt theo chỉ mục, sử dụng kết hợp với hàm enumerate:
    a = { 10, 2,3, 1, 3, 2, 10 }
    for index, value in enumerate(a):
        print(index, value)
        

5. Các phương thức của set

Một số phương thức thường hay sử dụng
    · add(e): thêm e vào tập hợp
    · clear(): xóa mọi phần tử trong tập hợp
    · copy(): tạo một bản sao của tập hợp
    · difference(x): tương đương với phép trừ đi x
    · difference_update(x): loại bỏ những phần tử trong x khỏi tập (cập nhật vào tập hiện tại)
    · discard(e): bỏ e khỏi tập
    · intersection(x): tương đương với phép giao với x
    · intersection_update(x): tương đương với phép giao với x (cập nhật vào tập hiện tại)
    
    · isdisjoint(x): trả về True nếu tập không có phần chung nào với x
    · issubset(x): trả về True nếu tập là con của x, tương đương với phép so sánh <= x
    · issuperset(x): trả về True nếu x là tập con của tập, tương đương với phép so sánh >=x
    · pop(): lấy một phần tử ra khỏi tập (không biết trước)
    · remove(e): bỏ e khỏi tập, báo lỗi nếu không tìm thấy e
    · symmetric_difference(x): tương đương với phép ^x
    · symmetric_difference_update(x): tương đương với phép ^x (cập nhật vào tập hiện tại)
    · union(x): tương đương với phép hợp với x
    · update(x): đưa các phần tử của tập x vào tập hiện tại

"""


"""		Frozenset (tập tĩnh)

Frozenset giống set, nhưng không thể bị thay đổi
    b = frozenset(((1,2),(2,3)))	#{(1,2),(2,3)}
    b.add ("abc")					# lỗi
    
Sự khác biệt giữa tập tĩnh và tập hợp:
    · Tập tĩnh là kiểu bất biến, tập hợp là kiểu khả biến (dù các thành phần của nó phải là bất biến)
    · Tập tĩnh thường nhanh và ít tốn bộ nhớ hơn tập hợp
    · Tập tĩnh không sử dụng được các phương thức thay đổi nội dung như add() hoặc remove()
    · Tập tĩnh vẫn hỗ trợ các phép toán của kiểu tập hợp (giao, hợp, hiệu, ... )
    · Tập tĩnh vẫn hỗ trợ các phép so sánh với tập hợp
    · Tập tĩnh có thể dùng làm khóa cho dữ liệu từ điển (học sau)

"""

s = { 'thay abc = ?' if x in 'abc' else x for x in 'abracadabra' }

print(s)




