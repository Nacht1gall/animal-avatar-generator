import logging
from math import floor
from typing import Any, Sequence

logger = logging.getLogger(__name__)

MIN = -(2 ** 31)
MAX = (2 ** 31) - 1


def pick(arr: Sequence, index: int) -> Any:
    try:
        new_index = integer(index, 0, len(arr) - 1)
        return arr[new_index]
    except IndexError as exc:
        logger.warning(exc, exc_info=True)
        return arr[0]


def integer(value: int, min_: int, max_: int) -> int:
    return floor(((value - MIN) / (MAX - MIN)) * (max_ + 1 - min_) + min_)
