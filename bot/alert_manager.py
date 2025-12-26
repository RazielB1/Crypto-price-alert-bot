def should_trigger(
    current_price: float,
    target_price: float,
    condition: str
) -> bool:
    if condition == "above":
        return current_price >= target_price
    elif condition == "below":
        return current_price <= target_price
    return False
