class CurrencyConverter:
    """A class to handle currency conversion operations."""
    
    def __init__(self, name, rate):
        """
        Initialize the converter with currency name and exchange rate.
        
        Args:
            name (str): Currency code (e.g., 'USD', 'EUR')
            rate (float): Exchange rate to INR
        """
        self.currency = name
        self.rate = rate

    def get_currency(self):
        """Return the currency code."""
        return self.currency

    def get_rate(self):
        """Return the current exchange rate."""
        return self.rate

    def set_currency(self, name):
        """Set a new currency code."""
        if not isinstance(name, str) or len(name) != 3:
            raise ValueError("Currency code must be a 3-letter string")
        self.currency = name

    def set_rate(self, rate):
        """Set a new exchange rate."""
        if rate <= 0:
            raise ValueError("Exchange rate must be positive")
        self.rate = rate

    def convert(self, amount):
        """
        Convert the given amount to INR.
        
        Args:
            amount (float): Amount to convert
            
        Returns:
            str: Formatted conversion result
        """
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        return f'{amount} {self.currency} is equal to {self.rate * amount:.2f} INR'

# Example usage
obj = CurrencyConverter('USD', 70)
print(obj.convert(100))

obj.set_currency('AUD')
obj.set_rate(50)
print(obj.convert(100))


# Key Concepts:
# Class with getter and setter methods
# Currency conversion logic
# Data validation (added)
# String formatting for output