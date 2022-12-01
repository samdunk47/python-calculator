class Basic_Calculator():
    def __init__(self) -> None:
        """ Initialises basic calculator class
        Returns: None
        """
        self.logic()
        self.user_input = None
    
    def logic(self) -> None:
        """ Controls the logic of the basic calculator
        Returns: None
        """
        self.user_input = self.take_input()
        self.term_array = self.create_term_array()
        self.result = self.evaluate_term_array()
        
    def take_input(self) -> str:
        """ Takes input from the user, removes whitespace
        Returns: str: modified input string
        """
        user_input = input("Enter expression: ")
        user_input = user_input.replace(" ", "")
        
        return user_input
        
    def create_term_array(self) -> list:
        """ Creates an array of all terms inputted
        Replaces "^" with "**" as python views "^" as bitwise XOR
        Ensures evaluation views it as exponentiation
        Returns: list: array of updated terms
        """
        terms = []
        current = None
        for char in self.user_input:
            current = char
            if char == "^":
                current = "**"
            terms.append(current)
            
        return terms

    def evaluate_term_array(self) -> float:
        """ Evaluates the term array
        Returns: float: evaluated terms
        """
        term_string = "".join(self.term_array)
        print(eval(term_string))
        
        
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