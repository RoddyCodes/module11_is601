import pytest
from app.operations.crud import perform_calculation
from app.operations.schemas import OperationType

def test_perform_calculation_add():
    """Tests a successful addition operation."""
    assert perform_calculation(10, 5, OperationType.add) == 15

def test_perform_calculation_subtract():
    """Tests a successful subtraction operation."""
    assert perform_calculation(20, 4, OperationType.subtract) == 16

def test_perform_calculation_multiply():
    """Tests a successful multiplication operation."""
    assert perform_calculation(7, 3, OperationType.multiply) == 21

def test_perform_calculation_divide():
    """Tests a successful division operation."""
    assert perform_calculation(100, 10, OperationType.divide) == 10

def test_perform_calculation_divide_by_zero():
    """Tests that dividing by zero correctly raises a ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        perform_calculation(5, 0, OperationType.divide)