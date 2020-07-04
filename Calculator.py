import math


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


def squared(a):
    return a * a


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        a = float(a)
        b = float(b)
        self.result = round(float(division(a, b)), 9)
        return self.result

    def square(self, a):
        self.result = squared(a)
        return self.result

    def radical(self, a):
        self.result = round(math.sqrt(float(a)), 8)
        return self.result
