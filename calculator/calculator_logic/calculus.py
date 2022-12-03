import calculator
        
class Quadratic_Calculator(calculus_type):
    def __init__(self) -> None:
        """ Initialises basic calculus class
        Returns: None
        """
        self.calculus_type = calculus_type
        self.logic()
        self.user_input = None
    
    def logic(self) -> None:
        """ Controls the logic of the calculus calculator
        Returns: None
        """
        print(calculus_type)
        quadratic_terms = self.take_input()
        if quadratic_terms == "invalid":
            calculator.restart()
        

    def take_input(self) -> list:
        """"""
        
        
        
        
        