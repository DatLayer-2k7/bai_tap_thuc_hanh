"""Exercise 02: compose Bot with a strategy."""

from collections.abc import Callable

State = dict[str, int]
Strategy = Callable[[State], str]


def move_toward_goal(state: State) -> str:
    """Move one step toward the goal, supporting goals at either end."""
    position = state["position"]
    goal = state["goal"]

    if position < goal:
        return "right"
    if position > goal:
        return "left"
    return "wait"


def defensive(state: State) -> str:
    """Wait when the opponent is adjacent; otherwise move toward the goal."""
    opponent = state.get("opponent_position")
    if opponent is not None and abs(opponent - state["position"]) <= 1:
        return "wait"
    return move_toward_goal(state)


def balanced(state: State) -> str:
    """Move directly toward the goal."""
    return move_toward_goal(state)


def aggressive(state: State) -> str:
    """Use direct goal-seeking movement for this exercise."""
    return move_toward_goal(state)


class Bot:
    """Choose actions using a replaceable strategy function."""

    def __init__(self, strategy: Strategy) -> None:
        self.strategy = strategy

    def choose_action(self, state: State) -> str:
        return self.strategy(state)


if __name__ == "__main__":
    state = {"position": 1, "opponent_position": 4, "goal": 4}
    for strategy in (defensive, balanced, aggressive):
        bot = Bot(strategy)
        print(strategy.__name__, bot.choose_action(state))

    # Swap strategies by changing the function passed to Bot,
    # not by modifying the Bot class.
    bot = Bot(defensive)
    print("swapped strategy:", bot.choose_action({"position": 3, "opponent_position": 4, "goal": 0}))
