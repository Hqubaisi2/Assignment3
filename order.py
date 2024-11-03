class Order:
    """
    Represents an order containing eBooks.
    """
    def __init__(self, order_id, ebooks, order_date):
        self.__order_id = order_id
        self.__ebooks = ebooks  # List of eBooks
        self.__order_date = order_date
        self.__total_price = self.calculate_total_price()

    def calculate_total_price(self):
        """
        Calculates the total price of the order before any discounts.
        """
        return sum(ebook.get_price() for ebook in self.__ebooks)

    def apply_discount(self, discount):
        """
        Applies a discount to the total price of the order.
        """
        self.__total_price = discount.apply(self.__total_price)

    def get_items(self):
        """
        Returns the list of eBooks in the order.
        """
        return self.__ebooks

    def get_total_price(self):
        """
        Returns the total price of the order.
        """
        return self.__total_price

    def __str__(self):
        return f"Order ID: {self.__order_id}, Total Price: {self.__total_price}"
