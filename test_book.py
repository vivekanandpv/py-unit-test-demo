import unittest
from book import BookStore


class BookTest(unittest.TestCase):

    def setUp(self) -> None:
        self.book_store = BookStore()

    def tearDown(self) -> None:
        pass

    def test_get_by_title(self):
        self.book_store.create_book('War and Peace', '12345')
        id = self.book_store.get_id_by_title('War and Peace')
        self.assertEqual('12345', id)

    def test_absent_title(self):
        with self.assertRaises(KeyError):
            id = self.book_store.get_id_by_title('The Idiot')

    @unittest.skip("Under development")
    def test_empty_store_has_integrity(self):
        self.assertTrue(self.book_store.has_integrity())
