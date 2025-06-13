def getFormattedNumber(number: int) -> str:
    if number is None:
        return None
    elif number >= 1_000_000_000:
        return f"{round(number / 1_000_000_000, 2)}B"
    elif number >= 1_000_000:
        return f"{round(number / 1_000_000, 2)}M"
    elif number >= 1_000:
        return f"{round(number / 1_000, 2)}K"
    else:
        return str(round(number, 2))