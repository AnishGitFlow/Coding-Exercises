class Orders:
    """A class to manage a shopping cart with items."""
    
    def __init__(self):
        """Initialize an empty cart."""
        self.cart = []

    def add_to_cart(self, item):
        """Add an item to the cart."""
        if not item:
            raise ValueError("Item cannot be empty")
        self.cart.append(item)

    def remove(self, item):
        """
        Remove an item from the cart.
        
        Raises:
            ValueError: If item is not in cart
        """
        if item not in self.cart:
            raise ValueError(f"Item '{item}' not found in cart")
        self.cart.remove(item)

    def __len__(self):
        """Return the number of items in cart."""
        return len(self.cart)
    
    def __str__(self):
        """Return a formatted string of cart contents."""
        if not self.cart:
            return "Cart is empty"
        items = "Cart Contents:\n"
        items += "\n".join(f"- {item}" for item in self.cart)
        return items
    
# Example usage
o = Orders()
o.add_to_cart('Soap')
o.add_to_cart('Paste')
o.add_to_cart('Brush')

print(f'Cart size: {len(o)}')
print(o)  # This will use __str__ method


# Key Concepts:
# List operations for cart management
# Magic methods (__len__, __str__)
# Basic CRUD operations (Create, Read, Update, Delete)
# String manipulation for display