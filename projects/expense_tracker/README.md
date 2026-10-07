# Personal Expense Tracker 💰

Ứng dụng quản lý chi tiêu cá nhân viết bằng Python.

## 1. Mục tiêu và ý nghĩa
Dự án giúp theo dõi các khoản chi tiêu hàng ngày, phân loại theo danh mục, tính tổng chi tiêu và tìm khoản chi lớn nhất, đảm bảo dữ liệu hợp lệ và dễ kiểm thử.

## 2. Các chức năng chính
1. **Thêm khoản chi (`add_expense`)**: Nhập danh mục, số tiền, mô tả. Tự động kiểm tra tính hợp lệ (tiền > 0, danh mục không rỗng).
2. **Tính tổng chi tiêu (`calculate_total`)**: Tính tổng số tiền đã chi tiêu (trả về 0.0 nếu danh sách rỗng).
3. **Lọc theo danh mục (`filter_by_category`)**: Lọc ra các khoản chi theo loại (Ăn uống, Học tập...) không phân biệt hoa thường.
4. **Tìm khoản chi lớn nhất (`get_highest_expense`)**: Tìm giao dịch chi nhiều tiền nhất.
5. **In báo cáo (`display_report`)**: Hiển thị bảng tổng hợp chi tiêu rõ ràng, định dạng tiền tệ đẹp mắt.

## 3. Cách chạy
- Chạy chương trình chính:
  ```bash
  python tracker.py
  ```
- Chạy kiểm thử (unit tests):
  ```bash
  python test_tracker.py
  ```
