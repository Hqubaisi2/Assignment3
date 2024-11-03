class Invoice:
    """
    Represents an invoice for an order, including VAT and any applicable discounts.
    """
    VAT_RATE = 0.05  # 5% VAT

    def __init__(self, invoice_id, order):
        self.__invoice_id = invoice_id
        self.__order = order

    def calculate_subtotal(self):
        """
        Calculates the subtotal (total cost of items before VAT).
        """
        return sum(item.get_price() for item in self.__order.get_items())

    def calculate_vat(self, subtotal):
        """
        Calculates the VAT based on the subtotal.
        """
        return subtotal * self.VAT_RATE

    def calculate_total(self, subtotal, vat):
        """
        Calculates the total cost including VAT.
        """
        return subtotal + vat

    def generate_invoice(self):
        """
        Generates a detailed invoice string with the subtotal, VAT, and total.
        """
        items = self.__order.get_items()
        subtotal = self.calculate_subtotal()
        vat = self.calculate_vat(subtotal)
        total = self.calculate_total(subtotal, vat)

        # Formatting the invoice details
        invoice_details = f"Invoice ID: {self.__invoice_id}\n"
        invoice_details += "Items Purchased:\n"

        for item in items:
            invoice_details += f"- {item.get_title()} (${item.get_price()})\n"

        invoice_details += f"\nSubtotal: ${subtotal:.2f}"
        invoice_details += f"\nVAT (5%): ${vat:.2f}"
        invoice_details += f"\nTotal with VAT: ${total:.2f}"

        return invoice_details
