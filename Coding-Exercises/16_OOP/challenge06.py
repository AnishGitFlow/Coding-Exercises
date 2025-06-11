class Customer:
    """A class to manage customer information with phone number validation."""
    
    def __init__(self, name, phoneno):
        """Initialize customer with name and phone number."""
        self.name = name
        self.phoneno = phoneno  # In a real app, validate phone number format

    def get_name(self):
        """Return the customer's name."""
        return self.name
    
    def get_phoneno(self):
        """Return the customer's phone number."""
        return self.phoneno
    
    def set_phoneno(self, ph):
        """Set a new phone number for the customer."""
        self.phoneno = ph

# Create customer object
c1 = Customer('Anish', 9999999999)

# Display initial details
print(f"Name: {c1.get_name()}")
print(f"Phone no: {c1.get_phoneno()}")

# Update phone number
c1.set_phoneno(8888888888)

# Display updated details
print(f"\nName: {c1.get_name()}")
print(f"Phone no: {c1.get_phoneno()}")


# Key Concepts:
# Getter and setter methods
# Encapsulation principle
# Object state modification
# Simple data management class