import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    # Позитивный тест №1

    def adding(self, x, y):
        return x + y

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 2, 2) == 4

    # Позитивный тест №2

    def subtraction(self, x, y):
        return x - y

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 4, 2) == 2