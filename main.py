import calculator

class App():
    def __init__(self) -> None:
        self.constants = calculator.generate_constants()
        self.begin()
    
    def begin(self) -> None:
        calculator.welcome_message()
        self.function_type = calculator.decide_calculator_function()

        
if __name__ == "__main__":
    app = App()
