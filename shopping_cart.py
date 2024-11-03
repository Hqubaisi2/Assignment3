class ShoppingCart:
    """
    Represents a shopping cart that can hold multiple eBooks.
    """
    def __init__(self):
        self.__items = []

    # Methods to add, remove, and clear the cart
    def add_ebook(self, ebook):
        self.__items.append(ebook)

    def remove_ebook(self, ebook):
        if ebook in self.__items:
            self.__items.remove(ebook)

    def clear_cart(self):
        self.__items = []

    def get_items(self):
        return self.__items

    def __str__(self):
        return f"Shopping Cart: {[str(item) for item in self.__items]}"
