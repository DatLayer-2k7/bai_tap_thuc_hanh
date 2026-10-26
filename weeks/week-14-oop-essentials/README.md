# Tuần 14 — OOP dễ nhớ: Class, Composition và Inheritance

> **Câu nhớ nhanh:** Class là bản thiết kế; Object là đối tượng cụ thể; Composition là “dùng/có một”; Inheritance là “là một loại của”.

Mục tiêu tuần này là tổ chức code dễ đọc, tái sử dụng và thay đổi. Hãy hiểu ý nghĩa trước, không cần học thuộc từng dòng code.

## 1. Bản đồ kiến thức

| Khái niệm | Cách nhớ | Ví dụ |
|---|---|---|
| Class | Bản thiết kế | `class Progress:` |
| Object | Đối tượng tạo từ class | `progress = Progress(3, 4)` |
| Attribute | Dữ liệu của object | `self.completed` |
| Method | Hàm của object | `progress.percentage()` |
| Composition | Một object sử dụng thành phần khác | `Bot(strategy)` |
| Inheritance | Một class là một loại của class khác | `Dog(Animal)` |

## 2. Class và Object — “bản thiết kế và sản phẩm”

Class mô tả object lưu dữ liệu gì và làm được gì. Object là một đối tượng cụ thể được tạo từ class.

~~~python
class Progress:
    def __init__(self, completed, total):
        self.completed = completed
        self.total = total

    def percentage(self):
        return self.completed / self.total * 100

    def __str__(self):
        return f"Progress: {self.completed}/{self.total} ({self.percentage():.0f}%)"


progress = Progress(3, 4)
print(progress.percentage())  # 75.0
print(progress)               # Progress: 3/4 (75%)
~~~

- `class Progress:` khai báo bản thiết kế.
- `__init__` chạy khi tạo object để khởi tạo dữ liệu.
- `self` là object hiện tại.
- `self.completed`, `self.total` là attribute — dữ liệu được lưu trên object.
- `percentage()` là method — hành vi tính phần trăm.
- `__str__()` định nghĩa chuỗi dễ đọc khi dùng `print(object)`.

Trong ví dụ, `Progress(3, 4)` nghĩa là đã hoàn thành 3 trên tổng 4 phần.

## 3. Encapsulation — gom dữ liệu và hành vi liên quan

**Encapsulation (đóng gói)** là đặt dữ liệu và các hành vi liên quan vào cùng một nơi, thường là class. Ví dụ, `Progress` giữ tiến độ và tự tính phần trăm của tiến độ đó.

**Mẹo nhớ:** dữ liệu nào phục vụ nhiệm vụ nào thì đặt gần hành vi xử lý dữ liệu đó. Đóng gói không có nghĩa dữ liệu tự động bị ẩn hoặc được bảo vệ hoàn toàn.

## 4. Composition — “dùng một / lắp ghép”

Trong bài Bot, strategy là hàm quyết định hành động. Bot nhận một strategy thay vì tự cố định một cách đi duy nhất.

~~~python
def balanced(state):
    if state["position"] < state["goal"]:
        return "right"
    if state["position"] > state["goal"]:
        return "left"
    return "wait"


class Bot:
    def __init__(self, strategy):
        self.strategy = strategy

    def choose_action(self, state):
        return self.strategy(state)


bot = Bot(balanced)
print(bot.choose_action({"position": 1, "goal": 4}))  # right
~~~

Luồng chạy:

1. `Bot(balanced)` tạo Bot và đưa hàm `balanced` vào.
2. `choose_action(state)` yêu cầu Bot chọn hành động.
3. `self.strategy(state)` gọi hàm strategy đã được đưa vào.
4. Hàm trả về `left`, `right` hoặc `wait`.

Có thể tạo `Bot(defensive)` hoặc `Bot(aggressive)` mà không cần sửa class `Bot`.

**Mẹo nhớ:** Composition = lắp ghép thành phần; ở đây Bot *dùng một strategy*.

## 5. Strategy — đổi cách làm, giữ nguyên Bot

- **`defensive`**: thận trọng; ví dụ đứng yên khi đối thủ ở ngay cạnh.
- **`balanced`**: di chuyển về phía mục tiêu.
- **`aggressive`**: trong bài tập cơ bản cũng di chuyển thẳng về mục tiêu; đây là ví dụ học tập, chưa phải AI chiến đấu phức tạp.

Luôn xét vị trí mục tiêu: mục tiêu ở bên phải thì đi `right`; ở bên trái thì đi `left`; đã đến mục tiêu thì `wait`.

## 6. Inheritance — “là một loại của”

Inheritance (kế thừa) phù hợp khi class con thực sự là một loại của class cha.

~~~python
class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def speak(self):
        return f"{self.name}: woof"


dog = Dog("Milo")
print(dog.speak())  # Milo: woof
~~~

- `Animal` là class cha.
- `Dog(Animal)` là class con.
- `Dog` có thể dùng `self.name` được khởi tạo ở `Animal`.
- `speak()` là hành vi được thêm riêng cho `Dog`.

**Mẹo nhớ:** Inheritance = **is-a** — Dog *là một* Animal. Đừng kế thừa chỉ để tái sử dụng vài dòng code. Nếu chỉ cần sử dụng một thành phần hoặc chiến lược, Composition thường linh hoạt hơn.

## 7. Chọn khái niệm nào?

| Câu hỏi | Khái niệm |
|---|---|
| Cần bản thiết kế để tạo object? | Class |
| Nói về một đối tượng cụ thể? | Object |
| Muốn thay hành vi bằng cách đưa thành phần khác vào? | Composition |
| Class này thực sự là một loại của class kia? | Inheritance |

## 8. Lỗi hay gặp

- Quên `self` ở tham số đầu tiên của method instance.
- Viết `percentage` thay vì gọi `percentage()` khi cần kết quả.
- Để `total = 0` rồi chia; trong bài Progress, tổng phải dương.
- Nhét mọi chiến lược vào class Bot, khiến khó thay đổi.
- Dùng inheritance khi quan hệ “is-a” không hợp lý.
- Chỉ thử Bot đi phải, quên thử mục tiêu bên trái và trường hợp đã đến đích.

## 9. Tự kiểm tra trong 30 giây

Thử trả lời trước khi xem đáp án:

1. Class khác Object thế nào?
2. `__init__` dùng để làm gì?
3. Trong `Bot(balanced)`, hàm `balanced` có vai trò gì?
4. Vì sao đổi strategy không cần sửa class Bot?
5. Vì sao `Dog(Animal)` là inheritance?
6. Bot ở vị trí 3, mục tiêu 0 thì đi hướng nào?

**Đáp án ngắn:** bản thiết kế / đối tượng cụ thể; khởi tạo dữ liệu; cung cấp cách chọn hành động; Bot gọi strategy được truyền vào; Dog là một Animal; `left`.

## 10. Thứ tự học và làm bài

1. Đọc [examples](examples/).
2. Làm [exercises](exercises/): `Progress`, `Bot` + strategy, `Animal`/`Dog`.
3. Nếu mắc, xem [hints](hints.md).
4. Chạy kiểm tra theo [checks](checks/README.md).
5. Áp dụng kiến thức trong [mini-project](mini-project/README.md).

> **Câu thần chú:** Class tạo khuôn — Object là đối tượng — Composition là “dùng một” — Inheritance là “là một loại”.
