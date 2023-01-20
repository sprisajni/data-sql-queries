# pylint: disable-all
import unittest
import sqlite3
from memoized_property import memoized_property
import subprocess

from queries import top_five_youngest_newly_directors

class TestTopFiveYoungestNewlyDirectors(unittest.TestCase):

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
        results = top_five_youngest_newly_directors(self.db)
        expected = []
        self.assertEqual(type(results), type(expected))

    def test_length_list(self):
        results = top_five_youngest_newly_directors(self.db)
        self.assertEqual(len(results), 5)

    def test_first_element(self):
        results = top_five_youngest_newly_directors(self.db)
        expected = [
            ("Adam Paloian", 8),
            ("Alfonso Ribeiro", 19),
            ("Kenn Navarro", 20),
            ("Xavier Dolan", 20),
            ("Albert Hughes", 21)
        ]
        self.assertEqual(results, expected)
