def add_numbers(a, b):
    return a + b


def rename_ai_value(value):
    if not isinstance(value, str):
        return str(value)
    renamed = value.replace("ai", "claude")
    return renamed
