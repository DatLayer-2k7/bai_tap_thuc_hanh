"""Exercise 04: a small regular-expression lab."""

import re  # noqa: F401 — learner uses this import to complete the TODOs.

text = "Tickets PJ-101 and PJ-205 are open; XX-999 is unrelated."

# TODO 1: use re.findall and r"PJ-\d{3}" to extract both course codes.
# Giải thích:
# - r"PJ-\d{3}" = tìm "PJ-" theo sau bởi 3 chữ số
# - re.findall() = trả về list tất cả kết quả tìm được
codes: list[str] = re.findall(r"PJ-\d{3}", text)


# TODO 2: use re.search to find the first number sequence.
# Giải thích:
# - r"\d+" = một hoặc nhiều chữ số liên tiếp
# - re.search() = tìm kết quả đầu tiên
# - .group() = lấy giá trị của kết quả tìm được
match = re.search(r"\d+", text)
first_number = match.group() if match else None


# TODO 3: use re.fullmatch to validate W followed by exactly two digits.
# Giải thích:
# - r"W\d{2}" = "W" theo sau bởi đúng 2 chữ số
# - re.fullmatch() = kiểm tra toàn bộ chuỗi phải khớp hoàn toàn
# - trả về match object nếu khớp, None nếu không
candidate = "W04"
is_week_code = re.fullmatch(r"W\d{2}", candidate) is not None


print("--- TODO 1: Tìm course codes ---")
print(f"Codes: {codes}")
print(f"Kết quả: {codes}")  # ['PJ-101', 'PJ-205']

print("\n--- TODO 2: Tìm số đầu tiên ---")
print(f"Text: {text}")
print(f"First number: {first_number}")  # '101'

print("\n--- TODO 3: Validate week code ---")
print(f"Candidate: {candidate}")
print(f"Is week code: {is_week_code}")  # True
