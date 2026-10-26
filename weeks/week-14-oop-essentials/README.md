# Tuần 14 — OOP dễ nhớ: Class, Composition và Inheritance

> **Nhớ trong 1 câu:** Class là bản thiết kế, Object là thứ được tạo ra từ bản thiết kế; Composition là “có/sử dụng một thứ”; Inheritance là “là một loại của thứ khác”.

Tuần này học cách tổ chức code để dễ đọc, tái sử dụng và thay đổi. Không cần học thuộc lòng mọi cú pháp — hãy hiểu mỗi phần giải quyết vấn đề gì.

## 1. Bản đồ kiến thức

| Khái niệm | Nhớ đơn giản | Ví dụ |
|---|---|---|
| **Class** | Bản thiết kế | **class Progress:** |
| **Object** | Một đối tượng tạo từ class | **progress = Progress(3, 4)** |
| **Attribute** | Dữ liệu của object | **self.completed** |
| **Method** | Hàm thuộc về object | **progress.percentage()** |
| **Composition** | Một object sử dụng thành phần được đưa vào | **Bot(strategy)** |
| **Inheritance** | Một class là một loại của class khác | **Dog(Animal)** |

## 2. Class và Object — “bản thiết kế và sản phẩm”

Class mô tả object có dữ liệu gì và làm được việc gì. Object là một đối tượng cụ thể được tạo từ class.

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

**Cách nhớ từng phần:**

- **class Progress:** — khai báo bản thiết kế.
- **__init__** — chạy khi tạo object, dùng để khởi tạo dữ liệu.
- **self** — chính object hiện tại.
- **self.completed** và **self.total** — dữ liệu được lưu trên object.
- **percentage()** — method tính phần trăm.
- **__str__()** — cách biểu diễn object thành chuỗi dễ đọc khi dùng **print()**.

Ở đây **Progress(3, 4)** tạo object có 3 phần hoàn thành trên tổng 4 phần.

## 3. Encapsulation — gom những thứ thuộc cùng trách nhiệm

**Encapsulation (đóng gói)** là tổ chức dữ liệu và hành vi liên quan trong cùng một nơi, thường là class. Ví dụ, **Progress** giữ số phần đã hoàn thành và phương thức tính phần trăm.

Mẹo nhớ: **dữ liệu nào phục vụ nhiệm vụ nào thì đặt gần hành vi xử lý dữ liệu đó**. Đóng gói không có nghĩa là mọi dữ liệu đều tự động bị ẩn hoặc được bảo vệ hoàn toàn.

## 4. Composition — “có một / sử dụng một”

Composition cho phép một object sử dụng thành phần khác thay vì tự viết tất cả hành vi vào một class.

Trong bài Bot, **strategy là một hàm quyết định hành động**. Bot nhận hàm đó khi được tạo:

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
action = bot.choose_action(
    {"position": 1, "goal": 4}
)
print(action)  # right
~~~

Luồng chạy:

1. **Bot(balanced)** — tạo Bot và đưa chiến lược **balanced** vào.
2. **choose_action(state)** — yêu cầu Bot chọn hành động.
3. **self.strategy(state)** — Bot gọi chiến lược đã nhận.
4. Hàm chiến lược trả về **left**, **right** hoặc **wait**.

Có thể đổi sang **Bot(defensive)** hoặc **Bot(aggressive)** mà không cần sửa class **Bot**.

**Mẹo nhớ:** Composition = **lắp ghép / đưa thành phần vào**. Trong bài này, Bot *dùng một strategy*.

## 5. Strategy — thay cách làm, giữ nguyên Bot

Ba strategy của bài tập:

- **defensive** — ưu tiên thận trọng; ví dụ, đứng yên nếu đối thủ ở ngay cạnh.
- **balanced** — đi về phía mục tiêu.
- **aggressive** — trong bài tập cơ bản này cũng đi thẳng về mục tiêu; đây là ví dụ đơn giản, chưa phải AI chiến đấu phức tạp.

Một điểm dễ sai: khi mục tiêu ở bên trái, Bot phải đi **left**; khi mục tiêu ở bên phải, Bot đi **right**; nếu đã đến mục tiêu thì **wait**. Đừng giả định mục tiêu lúc nào cũng ở bên phải.

## 6. Inheritance — “là một loại của”

Inheritance (kế thừa) phù hợp khi một class thực sự là một loại của class khác.

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

- **Animal** là class cha.
- **Dog(Animal)** là class con kế thừa từ **Animal**.
- **Dog** dùng được **self.name** vì phần khởi tạo được kế thừa từ **Animal**.
- **speak()** là hành vi riêng được thêm vào **Dog**.

**Mẹo nhớ:** Inheritance = **is-a** — Dog *là một* Animal.

Đừng dùng kế thừa chỉ để chia sẻ vài dòng code. Nếu một object chỉ cần sử dụng một thành phần hoặc chiến lược, Composition thường linh hoạt hơn.

## 7. Phân biệt nhanh

| Hãy tự hỏi | Dùng khái niệm |
|---|---|
| Tôi cần một bản thiết kế để tạo các object? | Class |
| Tôi đang nói về một đối tượng cụ thể? | Object |
| Tôi muốn object sử dụng một hành vi có thể thay thế? | Composition |
| Một class thực sự là một loại của class khác? | Inheritance |

## 8. Những lỗi hay gặp

- Quên **self** ở tham số đầu tiên của method instance.
- Viết **percentage** thay vì gọi **percentage()** khi cần kết quả.
- Chia cho **total = 0**; trong bài **Progress**, tổng phải dương.
- Viết logic strategy trực tiếp vào **Bot**, khiến việc đổi chiến lược khó hơn.
- Nghĩ rằng **Dog** có thể kế thừa từ bất kỳ class nào; chỉ nên kế thừa khi quan hệ “is-a” hợp lý.
- Chỉ thử trường hợp Bot đi sang phải, mà quên kiểm tra mục tiêu bên trái và trường hợp đã đến đích.

## 9. Tự kiểm tra trong 30 giây

Hãy thử trả lời mà không nhìn phần trên:

1. Class khác object ở điểm nào?
2. **__init__** dùng để làm gì?
3. Trong **Bot(balanced)**, **balanced** được đưa vào để làm gì?
4. Vì sao có thể đổi strategy mà không sửa class **Bot**?
5. Vì sao **Dog(Animal)** là ví dụ về inheritance?
6. Nếu Bot ở vị trí 3 và mục tiêu ở vị trí 0, hướng đi là gì?

**Đáp án ghi nhớ:** bản thiết kế / đối tượng cụ thể; khởi tạo dữ liệu; cung cấp hành vi chọn nước đi; Bot gọi strategy được truyền vào; Dog là một Animal; đi **left**.

## 10. Học và thực hành theo thứ tự

1. Đọc [examples](examples/).
2. Làm [exercises](exercises/) — ba bài về **Progress**, **Bot** + strategy, và **Animal**/**Dog**.
3. Nếu mắc, xem [hints](hints.md).
4. Chạy kiểm tra theo hướng dẫn trong [checks](checks/README.md).
5. Xem [mini-project](mini-project/README.md) để áp dụng kiến thức.

> **Câu thần chú:** Class tạo khuôn — Object là đối tượng — Composition là “dùng một” — Inheritance là “là một loại”.
