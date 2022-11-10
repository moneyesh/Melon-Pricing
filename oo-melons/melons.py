import random
from datetime import datetime

"""Classes for melon orders."""
class AbstractMelonOrder:

    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False


    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price() #splurge pricing 
        print(base_price)
        
        if self.species == "Christmas":
            base_price = 1.5*base_price

        
        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international" and self.qty < 10:
            total = total + 3
    
        return total

    def get_base_price(self):
        base_price = random.randint(5,9)
        
        this_day = datetime.today()
        week_day = this_day.isoweekday()
        time = this_day.hour
        print(f"{this_day}")
        print(f"day = {week_day}, time = {time}")
        
        if week_day < 6 and (time >= 8 and time <= 11):
            base_price = base_price + 4

        return base_price


    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17
    
    def __init__(self,species,qty,country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        self.country_code = country_code
        

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """An Government melon order."""

    tax = 0
    order_type = "government"
    passed_inspection = False

    def mark_inspection(self, passed):
        self.passed_inspection = passed