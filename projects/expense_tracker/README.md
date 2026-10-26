# Personal Expense Tracker 💰

Ứng dụng Python chạy trên terminal để theo dõi chi tiêu cá nhân. Có kiểm tra dữ liệu, thống kê, lọc danh mục và lưu dữ liệu vào JSON.

## Features
1. Thêm khoản chi với danh mục, số tiền dương và mô tả tùy chọn.
2. Xem báo cáo các khoản chi, tổng chi và khoản chi lớn nhất.
3. Lọc chi tiêu theo danh mục, không phân biệt hoa/thường.
4. Tính tổng chi tiêu; danh sách rỗng có tổng bằng 0.
5. Lưu/đọc dữ liệu JSON; nếu chưa có file thì bắt đầu với danh sách rỗng.

## Setup
Yêu cầu Python 3.10+ và pytest để chạy test. Ứng dụng không cần thư viện ngoài.

Tại thư mục gốc repository, cài pytest nếu máy chưa có:
```bash
python -m pip install pytest
```

## Usage
Chạy ứng dụng từ thư mục gốc:
```bash
python projects/expense_tracker/tracker.py
```
Chọn chức năng trong menu. Dữ liệu được lưu ở `projects/expense_tracker/expenses.json`. Không lưu thông tin tài chính riêng tư vào repository công khai.

Ví dụ báo cáo:
```text
- [Ăn uống] 45,000 đ (Cơm trưa)
Tổng chi tiêu: 45,000 đ
Khoản chi lớn nhất: Ăn uống (45,000 đ)
```

## Tests
Chạy kiểm thử:
```bash
python -m pytest projects/expense_tracker/test_tracker.py -q
```
Test bao gồm input hợp lệ/không hợp lệ, danh sách rỗng, lọc danh mục, khoản chi lớn nhất, lưu/đọc JSON, file không tồn tại và JSON lỗi.

## Design decisions
- Dùng list of dictionaries vì dữ liệu mỗi khoản chi nhỏ, dễ đọc và dễ kiểm thử.
- Tách logic thành hàm; input/output nằm trong `main()`.
- JSON dễ đọc, phù hợp ứng dụng cá nhân nhỏ; không phù hợp nhiều người dùng đồng thời.
- Khoản chi không hợp lệ trả về `False`; dữ liệu JSON hỏng báo `ValueError` thay vì âm thầm bỏ qua.

## Known limitations
- Ứng dụng terminal cho một người dùng; chưa có đăng nhập, mã hóa hoặc database.
- Số tiền dùng float nên đây là dự án học tập, không phải phần mềm kế toán.
- Chỉnh sửa/xóa giao dịch và báo cáo theo ngày chưa nằm trong phạm vi.

## AI usage
Xem [AI_USAGE.md](AI_USAGE.md). Hãy cập nhật phần khai báo này cho đúng với đóng góp thực tế của bạn.
