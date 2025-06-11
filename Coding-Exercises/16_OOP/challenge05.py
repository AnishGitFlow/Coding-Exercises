class Calculator:
    """A utility class for basic arithmetic operations."""
    
    @staticmethod
    def add(a, b):
        """Return the sum of two numbers."""
        return a + b
    
    @staticmethod
    def sub(a, b):
        """Return the difference between two numbers."""
        return a - b
    
    @staticmethod
    def mul(a, b):
        """Return the product of two numbers."""
        return a * b
    
    @staticmethod
    def div(a, b):
        """Return the quotient of two numbers."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

# Test values
x, y = 10, 3

# Perform and print all operations
print(f"The addition is: {Calculator.add(x, y)}")
print(f"The subtraction is: {Calculator.sub(x, y)}")
print(f"The multiplication is: {Calculator.mul(x, y)}")
print(f"The division is: {Calculator.div(x, y):.2f}")  # Format division result


# Key Concepts:
# Static methods (@staticmethod)
# Utility class pattern
# Basic arithmetic operations
# Error handling for division