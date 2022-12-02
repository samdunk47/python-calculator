import calculator

class App():
    """ App class - controls the program """    
    def __init__(self) -> None:
        """ Initialises the class """        
        self.constants = calculator.generate_constants()
        self.begin()
    
    def begin(self) -> None:
        """ Displays welcome message then decides type of calculator """        
        calculator.welcome_message()
        self.function_type = calculator.decide_calculator_function()
        match self.function_type:
            case "1":
                self.basic()
            case "2":
                self.quadratics()
            case "3":
                self.calculus()
            case "4":
                self.rearranging()
            case "5":
                self.surd_simplification()
    
    def basic(self) -> None:
        """ Controls the basic calculator """
        calculator.Basic_Calculator()
        
    
    def quadratics(self) -> None:
        """ Controls the quadratic calculator """
        calculator.Quadratic_Calculator()
        
    
    def calculus(self) -> None:
        """ Controls the calculus calculator """
        
        
    def rearranging(self) -> None:
        """ Controls the rearranging calculator """
        
        
    def surd_simplification(self) -> None:
        """ Controls the surd simplification calculator """
        calculator.Surd_Simplification_Calculator()
    
def restart():
    """ Restarts the program """
    app = App()
        

if __name__ == "__main__":
    app = App()
