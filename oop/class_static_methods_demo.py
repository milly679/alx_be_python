# oop/class_static_methods_demo.py

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method to add two numbers.
        Does not require access to the class or instance.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method to multiply two numbers.
        Can access class attributes and methods.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
