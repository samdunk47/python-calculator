import calculator

class Basic_Calculator():
    def __init__(self) -> None:
        """ Initialises basic calculator class
        Returns: None
        """
        self.logic()
    
    def logic(self) -> None:
        """ Controls the logic of the basic calculator
        Returns: None
        """
        user_input = self.take_input()
        term_array = self.create_term_array(user_input)
        result = self.evaluate_term_array(term_array)
        if result == "invalid":
            calculator.restart()
        
        print(result)
        
    def take_input(self) -> str:
        """ Takes input from the user, removes whitespace
        Returns: str: modified input string
        """
        user_input = input("Enter expression: ")
        user_input = user_input.replace(" ", "")
        
        return user_input
        
    def create_term_array(self, user_input) -> list:
        """ Creates an array of all terms inputted
        Replaces "^" with "**" as python views "^" as bitwise XOR
        Ensures evaluation views it as exponentiation
        Returns: list: array of updated terms
        """
        terms = []
        current = None
        for char in user_input:
            current = char
            if char == "^":
                current = "**"
            terms.append(current)
            
        return terms

    def evaluate_term_array(self, term_array) -> float:
        """ Evaluates the term array
        Returns: float: evaluated terms
        Returns: str: "invalid" if input is invalid
        """
        term_string = "".join(term_array)
        
        try:
            evaluated_answer = eval(term_string)
        except BaseException as error:
            print("Invalid input")
            return "invalid"
            
        return evaluated_answer
        
        
    # def add_numbers(*nums: float) -> float:
    #     """ Takes any number of real numbers as the argument
    #     Returns: float: sum of all numbers
    #     """
    #     total = 0
    #     for num in nums:
    #         total += num
            
    #     return total

    # def subtract_numbers(num1: float, num2: float) -> float:
    #     """ Takes any 2 real numbers as the argument 
    #     Returns: float: arg1 - arg2
    #     """    
    #     result = num1 - num2
        
    #     return result

    # def multiply_numbers(*nums: float) -> float:
    #     """ Takes any number of real numbers as the argument
    #     Returns: float: the product of all numbers passed in
    #     """    
    #     total = 0
    #     for num in nums:
    #         total *= num
            
    #     return total

    # def divide_numbers(num1: float, num2: float) -> float:
    #     """ Takes any 2 real numbers as the argument
    #     Returns: float: arg1 divided by arg2
    #     Conditions: num2 != 0
    #     """    
    #     result = num1 / num2
        
    #     return result