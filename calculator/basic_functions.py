from calculator import math

def add_numbers(*nums: float) -> float:
    """ Takes any number of real numbers as the argument

    Returns:
        float: the sum of all numbers passed in
    """    
    return sum(nums)

def subtract_numbers(num1: float, num2: float) -> float:
    """ Takes any 2 real numbers as the argument 
    
    Returns:
        float: num1 - num2 
    """    
    return num1 - num2

def multiply_numbers(*nums: float) -> float:
    """ Takes any number of real numbers as the argument

    Returns:
        float: the product of all numbers passed in
    """    
    return math.prod(nums)

def divide_numbers(num1: float, num2: float) -> float:
    """_summary_

    Args:
        num1 (float): any real number
        num2 (float): any real number, != 0

    Returns:
        float: num1 divided by num2
    """    
    return num1 / num2



