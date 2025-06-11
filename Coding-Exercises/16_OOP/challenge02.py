import math 

class Circle:
    """A class to represent a circle and perform geometric calculations."""
    
    def __init__(self, radius):
        """Initialize circle with given radius."""
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * self.radius ** 2  # Using exponent operator
    
    def perimeter(self):
        """Calculate and return the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius
    
# Create a circle with radius 7
obj = Circle(7)

# Print calculations with formatted output
print(f"The area of circle is: {obj.area():.2f}")
print(f"\nThe perimeter of circle is: {obj.perimeter():.2f}")


# Key Concepts:
# Mathematical calculations using math module
# Class methods for specific calculations
# String formatting (optimized)
# Error handling (added optimization)