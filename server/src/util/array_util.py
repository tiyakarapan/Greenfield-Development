from typing import Any, Callable, List


def find(arr: List[Any], equality_fn: Callable[[Any], bool]):
    return next((x for x in arr if equality_fn(x)))