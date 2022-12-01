import calculator

class App():
    def __init__(self) -> None:
        pass
    
    def begin(self) -> None:
        calculator.generate_constants()
        calculator.welcome_message()

        
if __name__ == "__main__":
    app = App()
    app.__init__()