# Week 06 — Iteration

## 1. `for` và `range`

```python
for number in range(1, 4):
    print(number)
```

`range(start, stop, step)` không gồm `stop`. Dùng `for` khi lặp qua một
iterable hoặc số lượt đã biết.

## 2. `while` và điều kiện dừng

```python
remaining = 3
while remaining > 0:
    print(remaining)
    remaining -= 1
```

Trước khi chạy, xác định biến nào làm điều kiện trở thành `False`.

## 3. `break` và `continue`

- `break` kết thúc loop hiện tại.
- `continue` bỏ qua phần còn lại của lượt hiện tại.

Giữ nhánh điều khiển ngắn để người đọc thấy luồng chạy.

## 4. `enumerate`

```python
topics = ["loops", "enumerate", "zip"]
for position, topic in enumerate(topics, start=1):
    print(position, topic)
```

Dùng `enumerate` khi cần cả vị trí và giá trị.

## 5. `zip`

```python
names = ["An", "Bình"]
scores = [8, 9]
for name, score in zip(names, scores, strict=True):
    print(name, score)
```

`strict=True` giúp phát hiện hai collection lệch độ dài trên Python 3.12+.

## 6. Comprehension đơn giản

```python
squares = [number**2 for number in range(1, 6)]
even_squares = [number**2 for number in range(1, 6) if number % 2 == 0]
```

Nếu cần nhiều nhánh, side effect hoặc comprehension lồng khó đọc, dùng loop
thường. Learner clarity quan trọng hơn việc rút ngắn code.

## 7. Cách vòng lặp hoạt động (Cơ chế trực quan)

- **`for` (Băng chuyền tự động):** 
  Máy tính tự lấy từng phần tử trong iterable (`range`, `list`, `str`) nạp vào biến lặp và thực thi khối code bên dưới. Khi hết phần tử, vòng lặp tự động dừng lại an toàn.
- **`while` (Người gác cổng kiểm tra điều kiện):** 
  Máy tính kiểm tra điều kiện trước mỗi lượt. Nếu điều kiện là `True`, chạy thân vòng lặp. Luôn phải cập nhật biến điều kiện (ví dụ: `remaining -= 1`) để điều kiện có lúc trở thành `False`, tránh gây ra **vòng lặp vô tận (infinite loop)**.
- **`break` vs `continue`:**
  - `break`: Dừng hẳn và nhảy vọt ra khỏi vòng lặp ngay lập tức.
  - `continue`: Bỏ qua phần còn lại của *lượt hiện tại* và nhảy sang lượt tiếp theo.

## 8. Khái niệm Biến trong Python

- **Bản chất:** Biến trong Python không phải là một "ô nhớ cố định" mà là một **"chiếc nhãn dán" (name reference)** trỏ tới đối tượng (`object`) nằm trong bộ nhớ.
- **Động (Dynamic Typing):** Bạn không cần khai báo kiểu dữ liệu trước (`int`, `float`, `str`). Kiểu dữ liệu gắn liền với chính giá trị/đối tượng, không gắn liền với tên biến.
- **Biến thiên:** Giá trị mà nhãn dán trỏ tới có thể thay đổi hoặc được gán lại sang đối tượng khác bất cứ lúc nào trong chương trình.

## 9. So sánh Biến: Python vs C++

| Tiêu chí | 🐍 Python | ⚡ C++ |
| :--- | :--- | :--- |
| **Hình tượng** | **Chiếc nhãn dán** trỏ vào đối tượng. | **Cái hộp (ô nhớ cố định)** trên RAM. |
| **Khai báo kiểu** | Không cần (`x = 5`). Tự nhận diện động. | Bắt buộc (`int x = 5;`). Kiểu tĩnh. |
| **Đổi kiểu giá trị** | Tự do đổi kiểu: `x = 5` rồi `x = "text"`. | Không thể đổi kiểu sau khi đã khai báo. |
| **Cơ chế gán (`b = a`)** | Gắn thêm nhãn `b` trỏ cùng đối tượng với `a`. | Sao chép giá trị từ `a` sang ô nhớ mới của `b`. |
| **Khai báo rỗng** | Không thể khai báo nếu chưa gán giá trị. | Cho phép `int x;` (chứa dữ liệu rác trong RAM). |
| **Bộ nhớ** | Tự động hoàn toàn (Garbage Collection). | Thủ công / Quản lý qua con trỏ và vùng nhớ. |

