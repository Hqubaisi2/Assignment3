class Discount:
    """
    Base class for all types of discounts.
    """
    def apply(self, total_price):
        return total_price  # No discount by default

class LoyaltyDiscount(Discount):
    """
    Discount for loyalty members.
    """
    def apply(self, total_price):
        return total_price * 0.9  # 10% discount for loyalty members

class BulkDiscount(Discount):
    """
    Discount for bulk orders.
    """
    def apply(self, total_price):
        return total_price * 0.85  # 15% discount for bulk orders
