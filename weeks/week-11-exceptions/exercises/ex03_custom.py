"""Exercise 03: reproduce and fix a defect."""


def distance(position: int, goal: int) -> int:
    # Reproduce the defect with (1, 4): old code returned a negative value.
    assert position <= goal, "position must be less than or equal to goal"
    return goal - position


print(distance(1, 4))
