
import operator
from .schemas import OperationType # Import the Enum from your schemas

def perform_calculation(a: float, b: float, op: OperationType) -> float:
    """
    A simple factory that maps an operation type to the correct math operation.
    """
    # This dictionary is the "factory"
    operation_map = {
        OperationType.add: operator.add,
        OperationType.subtract: operator.sub,
        OperationType.multiply: operator.mul,
        OperationType.divide: operator.truediv,
    }
    
    # Get the function from the map and execute it
    calculation_function = operation_map[op]
    return calculation_function(a, b)