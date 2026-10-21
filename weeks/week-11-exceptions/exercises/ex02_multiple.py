"""Exercise 02: defensive validation."""

LOCAL_ACTIONS = {"left", "right", "wait"}


def validate_action(action: str) -> str:
    if action not in LOCAL_ACTIONS:
        raise ValueError(
            f"Invalid action: {action!r}. Expected one of: {sorted(LOCAL_ACTIONS)}"
        )
    return action


print(validate_action("wait"))
