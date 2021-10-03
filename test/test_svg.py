import logging
from xml.etree import ElementTree
import unittest

from animal_avatar import Avatar
from animal_avatar.shapes import (
    EMPTY_SHAPE, BROWS, EARS,
    EYES, FACES, HAIRS,
    MUZZLES, PATTERNS
)

logger = logging.getLogger(__name__)


class TestAvatarShapes(Avatar):
    def __init__(self, *args, **kwargs):
        shapes = kwargs.pop('shapes')
        super().__init__(*args, **kwargs)
        self.shapes = shapes


class TestShapesSvg(unittest.TestCase):
    def test_svg(self):
        fake_seed = ''
        all_shapes = {
            'empty': [EMPTY_SHAPE],
            'brows': BROWS,
            'ears': EARS,
            'eyes': EYES,
            'faces': FACES,
            'hairs': HAIRS,
            'muzzles': MUZZLES,
            'patterns': PATTERNS
        }
        for shape_name, shapes in all_shapes.items():
            for i, shape in enumerate(shapes):
                avatar = TestAvatarShapes(fake_seed, shapes=[[shape]])
                try:
                    ElementTree.XMLParser().feed(avatar.create_avatar())
                    logger.info(f'{shape_name} - {i} is valid...')
                except Exception as exc:
                    self.fail(f'This SVG is not valid. Name: {shape_name}, index: {i}')


if __name__ == '__main__':
    unittest.main()
