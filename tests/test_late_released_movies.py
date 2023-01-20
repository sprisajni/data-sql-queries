# pylint: disable-all
import unittest
import sqlite3
from memoized_property import memoized_property
import subprocess

from queries import late_released_movies

class TestLateReleasedMovies(unittest.TestCase):
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
        results = late_released_movies(self.db)
        expected = []
        self.assertEqual(type(results), type(expected))

    def test_length_list(self):
        results = late_released_movies(self.db)
        self.assertEqual(len(results), 6)

    def test_first_element(self):
        results = late_released_movies(self.db)
        expected = [
            "Cars",
            "Fantasia 2000",
            "Game of Death",
            "The Many Adventures of Winnie the Pooh",
            "The Rescuers",
            "Waitress"
        ]
        self.assertEqual(set(results), set(expected))
