import pytest
from pydantic import ValidationError
from app.operations.schemas import CalculationCreate, CalculationRead, OperationType

def test_calculation_create_success():
    """Tests successful creation of a CalculationCreate schema."""
    calc_data = {"a": 20, "b": 5, "operation_type": OperationType.divide, "user_id": 1}
    calc = CalculationCreate(**calc_data)
    assert calc.a == 20
    assert calc.b == 5
    assert calc.user_id == 1

def test_calculation_create_division_by_zero_raises_error():
    """Tests that the custom validator prevents division by zero."""
    invalid_data = {"a": 10, "b": 0, "operation_type": OperationType.divide, "user_id": 1}
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        CalculationCreate(**invalid_data)

def test_calculation_create_invalid_type():
    """Tests that Pydantic's native validation catches incorrect data types."""
    invalid_data = {"a": "ten", "b": 5, "operation_type": OperationType.add, "user_id": 1}
    with pytest.raises(ValidationError):
        CalculationCreate(**invalid_data)

def test_calculation_read_from_orm_mode():
    """Tests creating a CalculationRead schema from a mock ORM object."""
    # Create a simple mock object with attributes, simulating a SQLAlchemy model instance
    class MockOrmModel:
        id = 1
        a = 100
        b = 20
        operation_type = OperationType.subtract
        result = 80.0
        user_id = 123

    orm_instance = MockOrmModel()
    # Pydantic V2 uses `model_validate` for ORM-compatible data loading
    calc_read = CalculationRead.model_validate(orm_instance)

    assert calc_read.id == 1
    assert calc_read.result == 80.0
    assert calc_read.user_id == 123
    assert calc_read.operation_type == OperationType.subtract