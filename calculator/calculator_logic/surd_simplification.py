class Surd_Simplification_Calculator():
    def __init__(self) -> None:
        """ Initialises basic calculator class
        Returns: None
        """
        self.logic()
        self.user_input = None
    
    def logic(self) -> None:
        """ Controls the logic of the surd simplification calculator
        Returns: None
        """

    def take_input(self) -> str:
        """ Takes input from the user
        Returns: str: inputted string
        """
        user_input = input("Enter expression: ")
        return user_input

    def find_factors(self, number: int) -> int:
        """ Takes integer argument, finds all factors of the integer
        Returns: list: array of integers
        """
        
        
        