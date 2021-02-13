import pytest
from app.calculator import Calculator


class TestCalculator:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculation_correctly(self):
        assert self.calc.multiply(self, 4, 5) == 20

    def test_division_calculation_correctly(self):
        assert self.calc.division(self, 10, 5) == 2

    def test_subtraction_calculation_correctly(self):
        assert self.calc.subtraction(self, 17, 7) == 10

    def test_adding_calculation_correctly(self):
        assert self.calc.adding(self, 6, 12) == 18


