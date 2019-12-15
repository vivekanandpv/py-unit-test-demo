import os


class BookStore:
    def __init__(self, dir_path):
        self.books = {}
        self.filename = os.path.join(dir_path, 'bookstore.txt')
        self.cache = open(self.filename, 'w')

    def create_book(self, title, id):
        self.books[title] = id

    def get_id_by_title(self, title):
        return self.books[title]

    def clean_up(self):
        self.cache.close()
        os.remove(self.filename)
