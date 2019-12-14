import unittest
from book import BookStore


class BookTest(unittest.TestCase):

    def test_get_by_title(self):
        book_store = BookStore()
        book_store.create_book('War and Peace', '12345')
        id = book_store.get_id_by_title('War and Peace')
        self.assertEqual('12345', id)

    def test_absent_title(self):
        book_store = BookStore()
        with self.assertRaises(KeyError):
            id = book_store.get_id_by_title('The Idiot')

    @unittest.skip("Under development")
    def test_empty_store_has_integrity(self):
        book_store = BookStore()
        self.assertTrue(book_store.has_integrity())
