from ebook import EBook
from customer import Customer
from order import Order
from invoice import Invoice
from discount import LoyaltyDiscount


def main():
    # Creating a customer
    customer = Customer("John Doe", "john.doe@example.com", loyalty_member=True)

    # Adding eBooks to the shopping cart
    ebook1 = EBook("Book One", "Author A", "2020-01-01", "Fiction", "12345", 20.0)
    ebook2 = EBook("Book Two", "Author B", "2021-05-05", "Sci-Fi", "67890", 25.0)

    customer.get_shopping_cart().add_ebook(ebook1)
    customer.get_shopping_cart().add_ebook(ebook2)

    # Creating an order
    order = Order("ORD001", customer.get_shopping_cart().get_items(), "2024-10-29")

    # Apply loyalty discount if applicable
    if customer.is_loyalty_member():
        loyalty_discount = LoyaltyDiscount()
        order.apply_discount(loyalty_discount)

    # Generating invoice
    invoice = Invoice("INV001", order)
    print(invoice.generate_invoice())


if __name__ == "__main__":
    main()
