"""
Bài tập 01: if/elif/else cơ bản 🔀
====================================
Mục tiêu: Viết câu lệnh điều kiện đúng cú pháp
"""

# TODO 1: Nhập tuổi, in ra nhóm tuổi
# < 13: "Thiếu nhi"
# 13-17: "Thiếu niên"
# 18-64: "Người lớn"
# >= 65: "Người cao tuổi"
age = int(input("Nhập tuổi của bạn: "))
if age < 13:
    print("Thiếu nhi")
elif age < 18:
    print("Thiếu niên")
elif age < 65:
    print("Người lớn")
else:
    print("Người cao tuổi")

# TODO 2: Nhập điểm (0-10), xếp loại:
# >= 9: Xuất sắc, >= 8: Giỏi, >= 6.5: Khá, >= 5: TB, < 5: Yếu
score = float(input("Nhập điểm của bạn (0-10): "))
if score >= 9:
    print("Xuất sắc")
elif score >= 8:
    print("Giỏi")
elif score >= 6.5:
    print("Khá")
elif score >= 5:
    print("TB")
else:
    print("Yếu")

# TODO 3: Nhập năm, kiểm tra năm nhuận
# Năm nhuận: chia hết cho 4, NHƯNG không chia hết cho 100,
# TRỪ KHI chia hết cho 400
# 2000 → nhuận, 1900 → không, 2024 → nhuận
public_year = int(input("Nhập năm: "))
if (public_year % 4 == 0 and public_year % 100 != 0) or (public_year % 400 == 0):
    print(f"{public_year} là năm nhuận")
else:
    print(f"{public_year} không phải là năm nhuận")

# TODO 4 (Thử thách): Nhập 3 số, in ra số lớn nhất
# KHÔNG dùng hàm max() — chỉ dùng if/elif/else
num1 = float(input("Nhập số thứ nhất: "))
num2 = float(input("Nhập số thứ hai: "))
num3 = float(input("Nhập số thứ ba: "))

if num1 >= num2 and num1 >= num3:
    print(f"Số lớn nhất là: {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"Số lớn nhất là: {num2}")
else:
    print(f"Số lớn nhất là: {num3}")