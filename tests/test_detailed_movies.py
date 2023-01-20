# pylint: disable-all
import unittest
import sqlite3
from memoized_property import memoized_property
import subprocess

from queries import detailed_movies

class TestDetailedMovies(unittest.TestCase):
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

    def test_is_list(self):
        results = detailed_movies(self.db)
        expected = []
        self.assertEqual(type(results), type(expected))

    def test_length_list(self):
        results = detailed_movies(self.db)
        self.assertEqual(len(results), 9872)

    def test_first_element(self):
        results = detailed_movies(self.db)
        result_0 = results[0]
        expected = (
            'A Trip to the Moon',
            'Action,Adventure,Comedy',
            'Georges Méliès'
        )
        self.assertEqual(result_0, expected)

    def test_len_each_tuple(self):
        results = detailed_movies(self.db)
        for r in results:
            self.assertEqual(len(r), 3)
