#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Python implementation of Animal Avatar Generator
(https://github.com/roma-lukashik/animal-avatar-generator).
Python >= 3.7

License: MIT
"""

__version__ = '0.0.2'
__license__ = 'MIT'

import random
from typing import Sequence

from animal_avatar.palette import AVATAR_COLORS, BACKGROUND_COLORS
from animal_avatar.shapes import (
    EMPTY_SHAPE, BROWS, EARS,
    EYES, FACES, HAIRS,
    MUZZLES, PATTERNS
)
from animal_avatar.utils.svg import create_svg, create_background, create_blackout


class Avatar:
    def __init__(self, seed: str, size: int = 150,
                 avatar_colors: Sequence = AVATAR_COLORS, background_colors: Sequence = BACKGROUND_COLORS,
                 blackout: bool = True, is_round: bool = True):
        self.rng = random.Random(seed)
        self.size = size
        self.avatar_color = self.rng.choice(avatar_colors)
        self.background_color = self.rng.choice(background_colors)
        self.blackout = blackout
        self.is_round = is_round
        self.avatar = None

        self.shapes = [
            FACES, self.optional(PATTERNS), EARS,
            self.optional(HAIRS), MUZZLES, EYES,
            BROWS
        ]

    def optional(self, shapes) -> Sequence:
        if self.rng.randrange(100) < 50:
            return shapes
        return (EMPTY_SHAPE, )

    def set_avatar(self) -> None:
        self.avatar = ''.join(map(lambda shape: self.rng.choice(shape)(self.avatar_color), self.shapes))

    def create_avatar(self) -> str:
        self.set_avatar()
        return create_svg(
            self.size,
            create_background(self.is_round, self.background_color),
            self.avatar,
            create_blackout(self.is_round) if self.blackout else ''
        )
