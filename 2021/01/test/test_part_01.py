import io

import unittest

from main import run_part_one, run_part_two

TEST_INPUT = """199
200
208
210
200
207
240
269
260
263"""

PART_ONE_TEST_RESULT = 7
PART_TWO_TEST_RESULT = 5

class TestDayOnePartOne(unittest.TestCase):
    def test_part_one(self):
        result = run_part_one(io.StringIO(TEST_INPUT))

        self.assertEqual(result, PART_ONE_TEST_RESULT)

    def test_part_two(self):
        result = run_part_two(io.StringIO(TEST_INPUT))

        self.assertEqual(result, PART_TWO_TEST_RESULT)

