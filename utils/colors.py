def darken(hex_str: str, amount: int) -> str:
    rgb = hex_to_rgb(hex_str)
    rgb_result = tuple(map(lambda x: clamp(x - amount, 0, 255), rgb))
    return rgb_to_hex(rgb_result)


def hex_to_rgb(hex_str: str) -> tuple:
    hex_ = hex_str.lstrip('#')
    return tuple(int(hex_[i:i+2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb: tuple) -> str:
    return '#' + ''.join(map(lambda x: (str(hex(x))[2:4]).zfill(2), rgb))


def clamp(value: int, min_: int, max_: int) -> int:
    return min(max_, max(min_, value))
