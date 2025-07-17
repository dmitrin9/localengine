import unittest
from search import search

class TestSearch(unittest.TestCase):
    def test_search(self):
        words = ["example", "hello", "this"]
        search(words)
if __name__ == "__main__":
    unittest.main()
