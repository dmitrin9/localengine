import unittest
from search import search

class TestSearch(unittest.TestCase):
    def test_search(self):
        words = ["example", "hello", "this"]
        rank = search(words)
        print(rank)
        self.assertTrue(len(rank))

        print("\n\n\n")

        words = ["example"]
        rank = search(words)
        print(rank)
        self.assertTrue(len(rank))

        words = ["this", "is", "an", "example", "1", "2", "hello"]
        rank = search(words)
        print(rank)
        self.assertTrue(len(rank))
if __name__ == "__main__":
    unittest.main()
