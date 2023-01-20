# pylint: disable-all
import unittest
import sqlite3
from memoized_property import memoized_property
import subprocess

from queries import stats_on

class TestStatsOn(unittest.TestCase):

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

    def test_is_dict(self):
        results = stats_on(self.db, "Action,Adventure,Comedy")
        expected = {}
        self.assertEqual(type(results), type(expected))

    def test_results_for_action_adv(self):
        results = stats_on(self.db, "Action,Adventure,Comedy")
        expected = {
            'genre': 'Action,Adventure,Comedy',
            'number_of_movies': 153,
            'avg_length': 100.98
        }
        self.assertEqual(results, expected)

    def test_results_for_drama(self):
        results = stats_on(self.db, "Drama,Mystery")
        expected = {
            'genre': 'Drama,Mystery',
            'number_of_movies': 23,
            'avg_length': 98.65
        }
        self.assertEqual(results, expected)
