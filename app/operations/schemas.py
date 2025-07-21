from pydantic import BaseModel, root_validator, ConfigDict 
from enum import Enum

# An Enum provides strong validation for the operation type
class OperationType(str, Enum):
    add = "Add"
    subtract = "Sub"
    multiply = "Multiply"
    divide = "Divide"

# A base schema to keep our code DRY (Don't Repeat Yourself)
class CalculationBase(BaseModel):
    a: float
    b: float
    operation_type: OperationType

# Schema for incoming data (creating a calculation)
class CalculationCreate(CalculationBase):
    user_id: int

    @root_validator(skip_on_failure=True)
    def check_division_by_zero(cls, values):
        # 'values' is a dictionary of all fields
        op_type = values.get('operation_type')
        b_val = values.get('b')

        if op_type == OperationType.divide and b_val == 0:
            raise ValueError("Division by zero is not allowed.")
        return values

# Schema for outgoing data (the API response)
class CalculationRead(CalculationBase):
    id: int
    result: float
    user_id: int

    # This tells Pydantic to read data from ORM models (SQLAlchemy)
    model_config = ConfigDict(from_attributes=True)