class Book:
    """A class to represent book information."""
    
    def __init__(self, title, author, price):
        """Initialize book attributes."""
        self.title = title
        self.author = author
        self.price = price

    def show_details(self):
        """Display all book details in a formatted way."""
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price:.2f}")  # Format price as currency
    
# Create a book object
obj = Book('Let us C', 'Yashwant Kanetkar', 800)

# Display book details
obj.show_details()


# Key Concepts:
# Simple class with attributes
# Method to display object information
# String formatting