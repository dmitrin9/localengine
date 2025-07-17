import unittest
from search import search

class TestSearch(unittest.TestCase):
    def test_search(self):
        words = ["example", "hello", "this"]
        rank = search(words)
        print(rank)
if __name__ == "__main__":
    unittest.main()
