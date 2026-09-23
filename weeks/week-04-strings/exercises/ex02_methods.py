"""
Bài tập 02: Phương thức chuỗi 🛠️
===================================
Mục tiêu: Dùng thành thạo các string methods
"""

# TODO 1: Cho email = "  User@Example.COM  "
# Chuẩn hóa email: xóa khoảng trắng, chuyển thường
# In kết quả: "user@example.com"
email = "  User@Example.COM  "
email = email.strip().lower()
print(email)

# TODO 2: Cho sentence = "hello world python programming"
# a) Chuyển thành Title Case: "Hello World Python Programming"
# b) Đếm số lần chữ "o" xuất hiện
# c) Thay "python" thành "PYTHON"
sentence = "hello world python programming"
sentence = sentence.title()
print(sentence)
print("Số lần chữ 'o' xuất hiện:", sentence.count('o'))
sentence = sentence.replace('Python', 'PYTHON')
print(sentence)

# TODO 3: Nhập họ tên đầy đủ, tách ra họ và tên
# Ví dụ: "Nguyễn Văn An" → Họ: "Nguyễn", Tên: "An"
# Gợi ý: dùng split() và indexing

full_name = input("Nhập họ tên đầy đủ: ")
name_parts = full_name.split()
ho = name_parts[0]
ten = name_parts[-1]
print(f"Họ: {ho}, Tên: {ten}")

# TODO 4: Kiểm tra tên file hợp lệ
# Nhập tên file, kiểm tra có kết thúc bằng .py, .txt, hoặc .csv không
# Gợi ý: dùng endswith()
print("Nhập tên file:")
file_name = input()
if file_name.endswith(('.py', '.txt', '.csv')):
    print("Tên file hợp lệ")
else:
    print("Tên file không hợp lệ")

# TODO 5 (Thử thách): Mã hóa Caesar
# Nhập chuỗi và số bước dịch (shift)
# Dịch mỗi ký tự đi shift bước trong bảng chữ cái
# "abc" với shift=3 → "def"
print("Nhập chuỗi để mã hóa:")
text = input()
shift = int(input("Nhập số bước dịch (shift): "))
encoded = ""
for char in text:
    if char.isalpha():
        base = ord('A') if char.isupper() else ord('a')
        encoded += chr((ord(char) - base + shift) % 26 + base)
    else:
        encoded += char
print("Chuỗi mã hóa:", encoded)