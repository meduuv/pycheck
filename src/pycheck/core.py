from collections.abc import Iterable
from numbers import Number


def is_int(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def is_number(value: object) -> bool:
    return isinstance(value, Number) and not isinstance(value, bool)


def is_non_empty(value: object) -> bool:
    try:
        return len(value) > 0  # type: ignore[arg-type]
    except TypeError:
        return False


def all_valid(values: Iterable[object], predicate) -> bool:
    return all(predicate(value) for value in values)
