class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __add__(self, other):
        return self.salary + other.salary

    def __sub__(self, other):
        return self.salary - other.salary

emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)

print("Total Salary:", emp1 + emp2)
print("Salary Difference:", emp1 - emp2)