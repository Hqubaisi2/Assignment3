class EBook:
    """
    Represents an eBook with various attributes like title, author, and price.
    """
    def __init__(self, title, author, publication_date, genre, isbn, price):
        self.__title = title
        self.__author = author
        self.__publication_date = publication_date
        self.__genre = genre
        self.__isbn = isbn
        self.__price = price  # Adding the price attribute

    # Getter and setter methods for each attribute, including price
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_publication_date(self):
        return self.__publication_date

    def get_genre(self):
        return self.__genre

    def get_isbn(self):
        return self.__isbn

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def __str__(self):
        return f"{self.__title} by {self.__author}, ISBN: {self.__isbn}, Price: {self.__price}"
