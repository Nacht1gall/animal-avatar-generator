from typing import Sequence

from animal_avatar.palette import AVATAR_COLORS, BACKGROUND_COLORS
from animal_avatar.shapes import (
    EMPTY_SHAPE, BROWS, EARS,
    EYES, FACES, HAIRS,
    MUZZLES, PATTERNS
)
from animal_avatar.utils.array import pick
from animal_avatar.utils.rand import seed_random
from animal_avatar.utils.svg import create_svg, create_background, create_blackout


class Avatar:
    def __init__(self, seed: str, size: int = 150,
                 avatar_colors: Sequence = AVATAR_COLORS, background_colors: Sequence = BACKGROUND_COLORS,
                 blackout: bool = True, is_round: bool = True):
        self.rng = seed_random(seed)
        self.size = size
        self.background_color = pick(background_colors, self.rng())
        self.avatar_color = pick(avatar_colors, self.rng())
        self.blackout = blackout
        self.is_round = is_round
        self.avatar = None

        self.shapes = [
            FACES, self.optional(PATTERNS), EARS,
            self.optional(HAIRS), MUZZLES, EYES,
            BROWS
        ]

    def optional(self, shapes: Sequence) -> tuple:
        return tuple(shape if self.rng() % 2 else EMPTY_SHAPE for shape in shapes)

    def set_avatar(self) -> None:
        self.avatar = ''.join(
            map(lambda shape: pick(shape, self.rng())(self.avatar_color), self.shapes)
        )

    def create_avatar(self) -> str:
        self.set_avatar()
        return create_svg(
            self.size,
            create_background(self.is_round, self.background_color),
            self.avatar,
            create_blackout(self.is_round) if self.blackout else ''
        )
