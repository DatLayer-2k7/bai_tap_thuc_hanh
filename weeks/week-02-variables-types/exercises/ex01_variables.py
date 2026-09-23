"""
Bài tập 01: Biến trong Python 📦
=================================
Mục tiêu: Hiểu cách khai báo và sử dụng biến
"""

# TODO 1: Tạo 4 biến lưu thông tin cá nhân
# ten = ???       (str)
# tuoi = ???      (int)
# diem_tb = ???   (float)
# dang_hoc = ???  (bool)
ten = "DatLayer"
tuoi = 18
diem_tb = 9.5
dang_hoc = True
# In ra giá trị và kiểu dữ liệu của mỗi biến bằng type()
print("Tên:", ten, "Kiểu dữ liệu:", type(ten))
print("Tuổi:", tuoi, "Kiểu dữ liệu:", type(tuoi))
print("Điểm trung bình:", diem_tb, "Kiểu dữ liệu:", type(diem_tb))
print("Đang học:", dang_hoc, "Kiểu dữ liệu:", type(dang_hoc))

# TODO 2: Hoán đổi giá trị 2 biến KHÔNG dùng biến tạm
# a = 10
# b = 20
# Sau hoán đổi: a = 20, b = 10
# Gợi ý: Python cho phép a, b = b, a
a = 10
b = 20
print("Trước hoán đổi: a =", a, ", b =", b)
a, b = b, a
print("Sau hoán đổi: a =", a, ", b =", b)

# TODO 3: Augmented assignment
# Cho x = 100. Dùng +=, -=, *=, //= để biến đổi x qua 4 bước
# In ra x sau mỗi bước
x = 100
print("Giá trị ban đầu của x:", x)
x += 50
print("Sau khi x += 50:", x)
x -= 30
print("Sau khi x -= 30:", x)
x *= 2
print("Sau khi x *= 2:", x)
x //= 3
print("Sau khi x //= 3:", x)

# TODO 4 (Thử thách): Multiple assignment
# Gán 3 biến trên 1 dòng: ho, ten, tuoi = ???
# In ra: "Họ tên: [ho] [ten], [tuoi] tuổi"
ho, ten, tuoi = "Truong", "Thanh Dat", 19
print("Họ tên:", ho, ten, ",", tuoi, "tuổi")