"""Some examples of tender, loving function definitions."""


def love(name: str) -> str:
    """Given a name as a paramter, returns a loving string."""
    return f"I love you {name}!"


def spread_love(to: str, n: int) -> str:
    """Generates a string that repeats a loving message n times."""
    love_note: str = ""
    c: int = 0
    while c < n:
        love_note += love(to) + "\n"
        c += 1
    return love_note