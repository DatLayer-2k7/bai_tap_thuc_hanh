"""
Bài tập 03: f-string formatting 💅
====================================
Mục tiêu: Định dạng output đẹp với f-string
"""

# TODO 1: Cho ten = "An", tuoi = 20, diem = 8.567
# In ra: "Học sinh An, 20 tuổi, điểm TB: 8.57"
# Gợi ý: dùng :.2f để làm tròn 2 chữ số thập phân
print("--- TODO 1: Định dạng thập phân ---")
ten = "An"
tuoi = 20
diem = 8.567
print(f"Học sinh {ten}, {tuoi} tuổi, điểm TB: {diem:.2f}")


# TODO 2: In bảng cửu chương 5 với cột thẳng hàng
# Dùng f-string width: f"{value:>4}"
# 5 x  1 =   5
# 5 x  2 =  10
# ...
# 5 x 10 =  50
print("\n--- TODO 2: Bảng cửu chương 5 ---")
for i in range(1, 11):
    ket_qua = 5 * i
    print(f"5 x {i:>2} = {ket_qua:>3}")


# TODO 3: In hóa đơn mua hàng đẹp
# Dùng f-string để căn lề trái/ph��i
# ===========================
# SẢN PHẨM          GIÁ (VNĐ)
# ---------------------------
# Cà phê              35,000
# Bánh mì             25,000
# Nước suối            10,000
# ---------------------------
# TỔNG CỘNG           70,000
# ===========================
# Gợi ý: dùng f"{name:<20}{price:>10,}"
print("\n--- TODO 3: Hóa đơn mua hàng ---")
print("=" * 35)
print(f"{'SẢN PHẨM':<20} {'GIÁ (VNĐ)':>14}")
print("-" * 35)

san_pham = [
    ("Cà phê", 35000),
    ("Bánh mì", 25000),
    ("Nước suối", 10000)
]

tong_tien = 0
for ten_sp, gia in san_pham:
    tong_tien += gia
    print(f"{ten_sp:<20} {gia:>14,}")

print("-" * 35)
print(f"{'TỔNG CỘNG':<20} {tong_tien:>14,}")
print("=" * 35)


# TODO 4 (Thử thách): Tạo progress bar bằng f-string
# Nhập phần trăm (0-100)
# In ra: [████████░░░░░░░░░░░░] 40%
print("\n--- TODO 4: Progress Bar ---")
phan_tram = int(input("Nhập phần trăm hoàn thành (0-100): "))

# Kiểm tra input hợp lệ
if phan_tram < 0 or phan_tram > 100:
    print("❌ Phần trăm phải từ 0 đến 100!")
else:
    # Tính số ký tự đầy (█) và trống (░)
    tong_ky_tu = 20
    so_day = int(tong_ky_tu * phan_tram / 100)
    so_trong = tong_ky_tu - so_day
    
    # Tạo progress bar
    thanh_tien_do = "█" * so_day + "░" * so_trong
    
    print(f"[{thanh_tien_do}] {phan_tram}%")
