"""Exercise 01: for, range, enumerate and zip."""

topics = ["loops", "enumerate", "zip"]
scores = [7, 8, 9]

# TODO: print numbers 1 through 5 with range.
def numbered_pairs(topics: list[str], scores: list[int]) -> list[str]:
    """Return ['1. loops: 7', '2. enumerate: 8', ...]."""
    lines = []
    pairs = zip(topics, scores, strict=True)
    for position, (topic, score) in enumerate(pairs, start=1):
        lines.append(f"{position}. {topic}: {score}")
    return lines

# TODO: print each topic with a one-based position using enumerate.
def multiplication_table(number: int) -> list[str]:
    """Return ['3 x 1 = 3', '3 x 2 = 6', ..., '3 x 10 = 30']."""
    table = []
    for factor in range(1, 11):
        table.append(f"{number} x {factor} = {number * factor}")
    return table

# TODO: pair topics and scores with zip(..., strict=True).

if __name__ == "__main__":
    pairs = numbered_pairs(TOPICS, SCORES)
    print("numbered_pairs:", pairs)

    table = multiplication_table(5)
    print("multiplication_table(5):", table)
print(topics, scores)
