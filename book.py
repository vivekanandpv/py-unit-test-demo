class BookStore:
    def __init__(self):
        self.books = {}

    def create_book(self, title, id):
        self.books[title] = id

    def get_id_by_title(self, title):
        return self.books[title]
