import logging
import unittest

from animal_avatar.utils import rand

logger = logging.getLogger(__name__)


class TestCustomRandom(unittest.TestCase):
    def test_custom_random(self):
        seeds = (
            'seed', 'test', 'some long string over there!'
        )
        expected_results = (
            (-2038275316, -1768109603, -78991410,
             2027661943, -1086530787, -1347268750),  # seed
            (-601360192, 1153614527, -1909411243,
             -1757539480, -13368863, -1643392315),  # test
            (716536168, 915459876, -1040233634,
             973569428, 1661533838, -403104606),  # some long string over there!
        )

        for i, seed in enumerate(seeds):
            rng = rand.seed_random(seed)
            expected_seed_results = expected_results[i]
            for j in range(6):
                result = rng()
                expected_result = expected_seed_results[j]
                if result != expected_result:
                    self.fail(f'Seed: {seed}, result: {result}, expected: {expected_result}')
            logger.info(f'Seed: "{seed}" is valid...')


if __name__ == '__main__':
    unittest.main()
