from shopping_cart import ShoppingCart

class Customer:
    """
    Represents a customer with a name, email, and a shopping cart.
    """
    def __init__(self, name, email, loyalty_member=False):
        self.__name = name
        self.__email = email
        self.__loyalty_member = loyalty_member
        self.__shopping_cart = ShoppingCart()  # Each customer has a shopping cart

    # Getter methods for customer attributes
    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def is_loyalty_member(self):
        return self.__loyalty_member

    def get_shopping_cart(self):
        return self.__shopping_cart  # Method to return the shopping cart

    # Optional setter methods if you need to update customer attributes
    def set_name(self, name):
        self.__name = name

    def set_email(self, email):
        self.__email = email

    def set_loyalty_member(self, is_member):
        self.__loyalty_member = is_member

    def __str__(self):
        return f"Customer: {self.__name}, Email: {self.__email}, Loyalty Member: {self.__loyalty_member}"
