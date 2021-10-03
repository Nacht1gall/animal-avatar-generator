def create_svg(size: int, *children) -> str:
    return f"""
        <svg
            xmlns="http://www.w3.org/2000/svg"
            version="1.1"
            width="{size}"
            height="{size}"
            viewBox="0 0 500 500"
        >
            {''.join(children)}
        </svg>
    """


def create_background(is_round: bool, color: str) -> str:
    return f"""
        <rect
            width="500"
            height="500"
            rx="{250 if is_round else 0}"
            fill="{color}"
        />
    """


def create_blackout(is_round: bool) -> str:
    return f"""
        <path
            d="{'M250,0a250,250 0 1,1 0,500' if is_round else 'M250,0L500,0L500,500L250,500'}"
            fill="#15212a"
            fill-opacity="0.08"
        />
    """
