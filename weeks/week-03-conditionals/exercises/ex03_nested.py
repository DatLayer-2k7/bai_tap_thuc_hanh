"""
Bài tập 03: Điều kiện lồng nhau 🪆
====================================
Mục tiêu: Xử lý logic phức tạp với if lồng nhau
"""

# TODO 1: ATM rút tiền
# Nhập số dư hiện tại và số tiền muốn rút
# Kiểm tra: số tiền rút > 0? Đủ số dư không? Bội số 50,000?
# In thông báo phù hợp
print("Chào mừng bạn đến với ATM!")
so_du = float(input("Nhập số dư hiện tại: "))
so_tien_rut = float(input("Nhập số tiền muốn rút: "))
if so_tien_rut <= 0:
    print("Số tiền rút phải lớn hơn 0.")
elif so_tien_rut > so_du:
    print("Số dư không đủ.")
elif so_tien_rut % 50000 != 0:
    print("Số tiền rút phải là bội số của 50,000.")
else:
    so_du -= so_tien_rut
    print(f"Rút tiền thành công! Số dư còn lại: {so_du}")

# TODO 2: Xếp loại BMI
# Nhập chiều cao (m) và cân nặng (kg)
# BMI = weight / height^2
# < 18.5: Thiếu cân → gợi ý tăng cân
# 18.5-24.9: Bình thường → khen
# 25-29.9: Thừa cân → cảnh báo nhẹ
# >= 30: Béo phì → khuyến nghị gặp bác sĩ
chieu_cao = float(input("Nhập chiều cao (m): "))
can_nang = float(input("Nhập cân nặng (kg): "))
bmi = can_nang / (chieu_cao ** 2)
if bmi < 18.5:
    print(f"BMI của bạn là {bmi:.1f}. Thiếu cân. Hãy tăng cân!")
elif bmi < 25:
    print(f"BMI của bạn là {bmi:.1f}. Bình thường. Bạn rất khỏe mạnh!")
elif bmi < 30:
    print(f"BMI của bạn là {bmi:.1f}. Thừa cân. Hãy chú ý chế độ ăn uống!")
else:
    print(f"BMI của bạn là {bmi:.1f}. Béo phì. Hãy gặp bác sĩ để được tư vấn!")  

# TODO 3: Máy bán vé xem phim
# Nhập: loại vé (thuong/vip), ngày (thuong/cuoi_tuan), tuổi
# Giá cơ bản: thường 80k, VIP 120k
# Cuối tuần: +30%
# Trẻ em (<12) và người cao tuổi (>=65): giảm 50%
# Sinh viên (18-25): giảm 20%
# In giá vé cuối cùng
loai_ve = input("Nhập loại vé (thuong/vip): ").lower()
ngay = input("Nhập ngày (thuong/cuoi_tuan): ").lower()
tuoi = int(input("Nhập tuổi: "))    
# Thiết lập giá cơ bản
if loai_ve == 'vip':
    gia = 120000
else:
    gia = 80000

# Cuối tuần cộng 30%
if ngay == 'cuoi_tuan':
    gia *= 1.3

# Các mức giảm giá theo tuổi
if tuoi < 12 or tuoi >= 65:
    gia *= 0.5
elif 18 <= tuoi <= 25:
    gia *= 0.8

print(f"Giá vé cuối cùng: {int(gia)} VND")