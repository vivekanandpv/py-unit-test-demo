from book import BookStore
import pytest
import sys

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


# all markers are to be kept in pytest.ini in the root folder
@pytest.mark.slow
def test_which_is_slow(book_store):
    with pytest.raises(KeyError):
        id = book_store.get_id_by_title('The Idiot')

# to run this alone: python -m pytest -m custom_marker
# to exclude this: python -m pytest -m "not custom_marker"
# if PyCharm is used: additional arguments: -m "not x"
@pytest.mark.custom_marker
def test_which_is_custom(book_store):
    with pytest.raises(KeyError):
        id = book_store.get_id_by_title('The Idiot')


@pytest.mark.skip("In progress")
def test_which_is_skipped(book_store):
    with pytest.raises(KeyError):
        id = book_store.get_id_by_title('The Idiot')


@pytest.mark.skipif(sys.version_info < (3, 6), reason='requires Python 3.6 or higher')
def test_which_is_skipped_for_earlier_versions(book_store):
    with pytest.raises(KeyError):
        id = book_store.get_id_by_title('The Idiot')
