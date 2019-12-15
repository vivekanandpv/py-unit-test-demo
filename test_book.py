from book import BookStore
from pytest import *


@fixture
def book_store():
    bookstore = BookStore()
    yield bookstore
    bookstore.clean_up()


def test_get_by_title(book_store):
    book_store.create_book('War and Peace', '12345')
    id = book_store.get_id_by_title('War and Peace')
    assert '12345' == id


def test_absent_title(book_store):
    with raises(KeyError):
        id = book_store.get_id_by_title('The Idiot')
