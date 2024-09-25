from model.tools.validator import Validator
class Book:
    def __init__(self, id, title, author, isbn,language, genre):
        self.id = id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.language = language
        self.genre = genre

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = Validator.name_validator(title, "Invalid title")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        self._author = Validator.name_validator(author, "Invalid author")

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, isbn):
        self._isbn = Validator.isbn_validator(isbn, "Invalid ISBN")

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, language):
        self._language = Validator.language_validator(language, "Invalid language")

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, genre):
        self._genre = Validator.genre_validator(genre, "Invalid genre")
