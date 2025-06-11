from random import randint  # Import only what's needed

class Dice:
    """A class to simulate dice rolls with configurable sides."""
    
    def __init__(self, sides):
        """Initialize the dice with number of sides."""
        if sides < 1:
            raise ValueError("Dice must have at least 1 side")
        self.sides = sides

    def roll_dice(self):
        """Simulate a dice roll and return a random result."""
        return randint(1, self.sides)
    
# Create a 6-sided dice object
obj = Dice(6)

# Roll the dice twice and print results
print(obj.roll_dice())
print(obj.roll_dice())


# Key Concepts:
# Class definition and instantiation
# The __init__ constructor method
# Instance methods
# Random number generation
# Input validation (added optimization)