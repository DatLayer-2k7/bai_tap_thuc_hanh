# Notes — Bài tập lớp DienThoai (Python OOP)

## 1. Mục tiêu
Bài tập luyện cách tạo **class**, khởi tạo **object**, lưu dữ liệu bằng thuộc tính và hiển thị dữ liệu bằng phương thức.

## 2. Khái niệm cần nhớ

- **Class (lớp):** bản thiết kế để tạo các đối tượng. Ví dụ: `DienThoai`.
- **Object (đối tượng):** một điện thoại cụ thể được tạo từ lớp. Ví dụ: `DT01`, `DT02`.
- **Attribute (thuộc tính):** dữ liệu của đối tượng, gồm `MaMay`, `TenMay`, `HangSanXuat`, `DungLuongPin`, `GiaBan`.
- **Method (phương thức):** hàm nằm trong lớp, ví dụ `thongtindienthoai()`.
- **`__init__()`:** phương thức khởi tạo, tự chạy khi tạo đối tượng.
- **`self`:** tham chiếu đến đối tượng hiện tại. `self.TenMay = TenMay` lưu giá trị truyền vào thành thuộc tính của đối tượng.

## 3. Code mẫu

```python
class DienThoai:
    def __init__(self, MaMay, TenMay, HangSanXuat, DungLuongPin, GiaBan):
        self.MaMay = MaMay
        self.TenMay = TenMay
        self.HangSanXuat = HangSanXuat
        self.DungLuongPin = DungLuongPin
        self.GiaBan = GiaBan

    def thongtindienthoai(self):
        print("Mã máy:", self.MaMay)
        print("Tên máy:", self.TenMay)
        print("Hãng sản xuất:", self.HangSanXuat)
        print("Dung lượng pin:", self.DungLuongPin, "mAh")
        print("Giá bán:", self.GiaBan, "VNĐ")


if __name__ == "__main__":
    DT01 = DienThoai("DT01", "iPhone 15 Pro", "Apple", 3274, 28990000)
    DT02 = DienThoai("DT02", "Galaxy S24 Ultra", "Samsung", 5000, 29990000)

    DT01.thongtindienthoai()
    print("-" * 30)
    DT02.thongtindienthoai()
```

## 4. Chương trình hoạt động thế nào?

1. Khai báo lớp `DienThoai`.
2. Gọi `DienThoai(...)` để tạo một đối tượng; Python tự gọi `__init__()`.
3. Các dòng `self.ThuocTinh = gia_tri` lưu dữ liệu vào đối tượng.
4. Gọi `DT01.thongtindienthoai()` để in thông tin của DT01; gọi trên DT02 sẽ in thông tin DT02.

## 5. Vì sao dùng class?

Khi quản lý nhiều điện thoại, mỗi đối tượng có cùng cấu trúc nhưng dữ liệu riêng. Lớp giúp gom dữ liệu và hành vi liên quan vào một chỗ, dễ mở rộng thành chức năng tìm kiếm, cập nhật giá hoặc quản lý kho.

## 6. Mẹo nhớ khi kiểm tra

- Class = bản thiết kế.
- Object = đối tượng cụ thể.
- Attribute = dữ liệu.
- Method = hành động.
- `__init__` = khởi tạo dữ liệu.
- `self` = đối tượng hiện tại.
- Tên đúng của hàm khởi tạo là `__init__` (hai dấu gạch dưới ở đầu và cuối), không phải `__init_`.

## 7. Kết quả mong đợi

Chương trình in ra thông tin của iPhone 15 Pro (DT01), một đường phân cách, rồi thông tin của Galaxy S24 Ultra (DT02).
