# pylint: disable-all
import unittest
import sqlite3
from memoized_property import memoized_property
import subprocess

from queries import top_five_directors_for

class TestTopFiveDirectorsFor(unittest.TestCase):

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

    def test_return_list(self):
        results = top_five_directors_for(self.db, "Action,Adventure,Comedy")
        expected = []
        self.assertEqual(type(results), type(expected))

    def test_return_right_results1(self):
        results = top_five_directors_for(self.db, "Action,Adventure,Comedy")
        expected = [
            ('Robert Rodriguez', 5),
            ('Jonathan Frakes', 4),
            ('Anthony C. Ferrante', 3),
            ('Barry Sonnenfeld', 3),
            ('Jackie Chan', 3)
        ]
        self.assertEqual(results, expected)

    def test_return_5_results(self):
        results = top_five_directors_for(self.db, "Action,Adventure,Comedy")
        self.assertEqual(len(results), 5)

    def test_return_right_results2(self):
        results = top_five_directors_for(self.db, "Drama,Mystery")
        expected = [
            ('Aaron Schneider', 1),
            ('Alain Resnais', 1),
            ('Asghar Farhadi', 1),
            ('Bill Condon', 1),
            ('Chang-dong Lee', 1)
        ]
        self.assertEqual(results, expected)
