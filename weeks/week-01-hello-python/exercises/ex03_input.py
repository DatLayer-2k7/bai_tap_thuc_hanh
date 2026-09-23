"""
Bài tập 03: Trò chuyện với Python 💬
=====================================
Mục tiêu: Sử dụng input() để nhận dữ liệu từ người dùng
"""

# TODO 1: Hỏi tên người dùng và in lời chào
# Ví dụ: "Xin chào, Minh!"
print("Xin chào, " + input("Nhập tên của bạn: ") + "!")

# TODO 2: Hỏi tuổi người dùng, tính và in năm sinh
# Gợi ý: Nhớ chuyển input sang int!
print("Bạn sinh năm: " + str(2026 - int(input("Nhập tuổi của bạn: "))) + "!")

# TODO 3: Hỏi người dùng nhập 2 số, tính và in tổng
# Ví dụ output:
# Nhập số thứ nhất: 15
# Nhập số thứ hai: 27
# Tổng: 15 + 27 = 42
num1 = int(input("Nhập số thứ nhất: "))
num2 = int(input("Nhập số thứ hai: "))
print("Tổng: " + str(num1) + " + " + str(num2) + " = " + str(num1 + num2) + "!")

# TODO 4 (Thử thách): Tạo Mad Libs mini
# Hỏi người dùng nhập: tên, tính từ, con vật, số
# Rồi in ra câu chuyện vui
print("Một ngày nọ, " + input("Nhập tên: ") + " đi dạo trong rừng. "
      "Cậu ấy gặp một con " + input("Nhập tính từ: ") + " " + input("Nhập con vật: ") + " và nó nói: 'Chào! Bạn có " + input("Nhập số: ") + " quả táo không?'")