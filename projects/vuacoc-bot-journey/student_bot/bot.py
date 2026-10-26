"""Student Bot for the course-local Line Arena.

Week 14 focus: composition. A Bot receives a strategy rather than hardcoding
one policy, so strategies can be replaced without changing the Bot class.
"""

from collections.abc import Callable
from typing import TypeAlias

State: TypeAlias = dict[str, int]
Strategy: TypeAlias = Callable[[State], str]

ACTIONS = {"left", "right", "wait"}


def move_toward_goal(state: State) -> str:
    """Return one step toward the goal, or wait when already there."""
    position = state["position"]
    goal = state["goal"]
    if position < goal:
        return "right"
    if position > goal:
        return "left"
    return "wait"


def defensive(state: State) -> str:
    """Avoid moving when the opponent is immediately adjacent."""
    opponent = state.get("opponent_position")
    if opponent is not None and abs(opponent - state["position"]) <= 1:
        return "wait"
    return move_toward_goal(state)


def balanced(state: State) -> str:
    """Prioritize moving toward the goal."""
    return move_toward_goal(state)


def aggressive(state: State) -> str:
    """Use the direct goal-seeking policy for this local exercise."""
    return move_toward_goal(state)


class Bot:
    """Delegate action selection to a replaceable strategy."""

    def __init__(self, strategy: Strategy = balanced) -> None:
        self.strategy = strategy

    def choose_action(self, state: State) -> str:
        """Choose an action using the configured strategy."""
        action = self.strategy(state)
        if action not in ACTIONS:
            raise ValueError(f"strategy returned invalid action: {action!r}")
        return action


_default_bot = Bot()


def choose_action(state: State) -> str:
    """Backward-compatible entry point using the balanced strategy."""
    return _default_bot.choose_action(state)


def main() -> None:
    """Show that the bot can run with the local teaching state."""
    teaching_state = {
        "turn": 1,
        "max_turns": 6,
        "position": 0,
        "opponent_position": 4,
        "goal": 4,
        "min_position": 0,
        "max_position": 4,
    }
    print(choose_action(teaching_state))


if __name__ == "__main__":
    main()
