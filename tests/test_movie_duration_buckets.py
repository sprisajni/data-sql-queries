# pylint: disable-all
import unittest
import sqlite3
from memoized_property import memoized_property
import subprocess

from queries import movie_duration_buckets

class TestMovieDurationBuckets(unittest.TestCase):
    @memoized_property
    def stubs(self):
        # Download the database
        subprocess.call(
            [
                "curl", "https://wagon-public-datasets.s3.amazonaws.com/sql_databases/movies.sqlite", "--output",
                "data/movies.sqlite"
            ])

    def setUp(self):
        super().setUp()
        self.stubs
        conn = sqlite3.connect('data/movies.sqlite')
        self.db = conn.cursor()

    def test_movie_duration_buckets(self):
        res = movie_duration_buckets(self.db)
        solution = [
            (30, 292),
            (60, 764),
            (90, 1362),
            (120, 5302),
            (150, 1617),
            (180, 331),
            (210, 88),
            (240, 19),
            (270, 7),
            (300, 11),
            (330, 4),
            (360, 7),
            (390, 7),
            (420, 4),
            (450, 4),
            (480, 2),
            (540, 4),
            (570, 3),
            (600, 4),
            (630, 2),
            (690, 2),
            (900, 1),
            (1020, 1)
        ]
        self.assertIs(type(res), list)
        self.assertIs(type(res[0]), tuple)
        self.assertEqual(res, solution)
