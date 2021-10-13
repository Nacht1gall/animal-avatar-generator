MAX_INT32_HEX = 0x7FFFFFFF
MAX_UNSIGNED_INT32_HEX = 0xFFFFFFFF


def seed_random(seed: str):
    value = hash_(seed)

    def next_value() -> int:
        nonlocal value
        value = xor_shift32(value)
        return value

    return next_value


def xor_shift32(value: int) -> int:
    return shift_left(shift_right(shift_left(value, 13), 17), 5)


def shift_left(value: int, shift: int) -> int:
    result = (value & MAX_UNSIGNED_INT32_HEX) ^ ((value << shift) & MAX_UNSIGNED_INT32_HEX)
    return mimic_overflow(result)


def shift_right(value: int, shift: int) -> int:
    result = (value & MAX_UNSIGNED_INT32_HEX) ^ ((value >> shift) & MAX_UNSIGNED_INT32_HEX)
    return mimic_overflow(result)


def hash_(seed: str) -> int:

    def inner_function(h, x):
        return to_int32((h << 5) - h + x)

    result = 0  # initial value
    for character in list(seed):
        number = ord(character)
        result = inner_function(result, number)
    return result


def to_int32(x: int) -> int:
    x = x & MAX_UNSIGNED_INT32_HEX
    return mimic_overflow(x)


def mimic_overflow(x: int):
    """
    JavaScript stores all numbers as 64-bit floating point,
    but as soon as you start using bitwise operators
    the interpreter converts the number to a 32 bit representation.
    This function emulates this behavior.
    """
    if x <= MAX_INT32_HEX:
        return x
    return -(~(x - 1) & MAX_UNSIGNED_INT32_HEX)
