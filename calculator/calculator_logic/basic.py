class Basic_Calculator():
    def __init__(self) -> None:
        """ Initialises basic calculator class
        """
        self.logic()
    
    def logic(self) -> None:#
        """ Controls the logic of the basic calculator
        """
        self.user_input = self.take_input()
    
    def take_input(self) -> str:
        """ Takes input from the user, removes whitespace
        """
        user_input = input("Enter expression: ")
        user_input.replace(" ", "")
        terms = []
        for char in user_input:
            try
            
    
    def add_numbers(*nums: float) -> float:
        """ Takes any number of real numbers as the argument
        Returns: float: sum of all numbers
        """
        total = 0
        for num in nums:
            total += num
        return total

    def subtract_numbers(num1: float, num2: float) -> float:
        """ Takes any 2 real numbers as the argument 
        Returns: float: arg1 - arg2
        """    
        result = num1 - num2
        return result

    def multiply_numbers(*nums: float) -> float:
        """ Takes any number of real numbers as the argument
        Returns: float: the product of all numbers passed in
        """    
        total = 0
        for num in nums:
            total *= num
        return total

    def divide_numbers(num1: float, num2: float) -> float:
        """ Takes any 2 real numbers as the argument
        Returns: float: arg1 divided by arg2
        Conditions: num2 != 0
        """    
        result = num1 / num2
        return result