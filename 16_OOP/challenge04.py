class Employee:
    """A class to represent employees with auto-generated IDs."""
    
    employee_count = 101  # Class variable to track employee count
    
    def __init__(self, name, designation, salary):
        """Initialize employee with name, designation, and salary."""
        self.name = name
        self.designation = designation
        self.salary = salary
        self.eid = 'e' + str(Employee.employee_count)  # Generate employee ID
        Employee.employee_count += 1  # Increment class variable

    def show_details(self):
        """Display employee details."""
        print(f"Name: {self.name}")
        print(f"Eid: {self.eid}")
        print(f"Salary: {self.salary:,.2f}")  # Format with commas
        print(f"Designation: {self.designation}")

    @classmethod
    def total_emp(cls):
        """Return total number of employees created."""
        return cls.employee_count - 101
    
# Create employee objects
e1 = Employee('John', 'Manager', 100000)
e2 = Employee('Anish', 'Team Leader', 80000)

# Show details for each employee
e1.show_details()
print()  # Blank line for separation
e2.show_details()

# Display total employee count
print(f"\nTotal Employees: {Employee.total_emp()}")


# Key Concepts:
# Class variables vs instance variables
# Class methods (@classmethod)
# Automatic ID generation
# String formatting for numbers
# Object-oriented organization of employee data