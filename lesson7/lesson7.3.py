def second_index(text: str, some_str: str) -> int | None:
    first = text.index(some_str)
    second = text.find(some_str, first+1)
    if second != -1:
        return second
    else:
        return None

assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print("OK")