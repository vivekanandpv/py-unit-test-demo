from book import BookStore
import pytest

# using tmpdir fixture for clearing cache
@pytest.fixture
def book_store(tmpdir):
    '''provides an empty BookStore object'''
    return BookStore(tmpdir)


def test_get_by_title(book_store):
    book_store.create_book('War and Peace', '12345')
    id = book_store.get_id_by_title('War and Peace')
    assert '12345' == id


def test_absent_title(book_store):
    with pytest.raises(KeyError):
        id = book_store.get_id_by_title('The Idiot')
