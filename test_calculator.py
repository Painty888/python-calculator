class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return b - a

    def multiply(self, a, b):
        result = 0
        negative = False

        # Handle negative numbers
        if b < 0:
            b = -b
            negative = not negative
        if a < 0:
            a = -a
            negative = not negative

        for _ in range(b):  # Corrected loop: range(b)
            result = self.add(result, a)

        return -result if negative else result

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Division by zero is undefined.")

        result = 0
        negative = False

        # Handle negative numbers
        if a < 0:
            a = -a
            negative = not negative
        if b < 0:
            b = -b
            negative = not negative

        while a >= b:  # Fixed condition: a >= b
            a = self.subtract(a, b)
            result += 1

        return -result if negative else result

    def modulo(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Modulo by zero is undefined.")

        negative = False

        # Handle negative numbers
        if a < 0:
            a = -a
            negative = not negative
        if b < 0:
            b = -b

        while a >= b:  # Fixed condition: a >= b
            a = self.subtract(a, b)

        return -a if negative else a
