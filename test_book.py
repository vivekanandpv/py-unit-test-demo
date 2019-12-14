import unittest
from book import BookStore


class BookTest(unittest.TestCase):

    def test_get_by_name(self):
        book_store = BookStore()
        book_store.create_book('War and Peace', '12345')
        id = book_store.get_id_by_name('War and Peace')
        self.assertEqual('12345', id)
