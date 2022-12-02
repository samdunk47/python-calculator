import calculator
        
class Quadratic_Calculator():
    def __init__(self) -> None:
        """ Initialises basic calculator class
        Returns: None
        """

        self.logic()
        self.user_input = None
    
    def logic(self) -> None:
        """ Controls the logic of the quadratic calculator
        Returns: None
        """
        quadratic_terms = self.take_input()
        if quadratic_terms == "invalid":
            calculator.restart()
        results = self.calculate_quadratic(quadratic_terms)
        self.output_results(results)
        

    def take_input(self) -> list:
        """ Takes 3 float inputs from user
        Returns: list: array of 3 floats
        """
        
        print("Ensure quadratic is in the form ax^2 + bx + c")
        try:
            quadratic_a = int(input("Enter a: "))
            quadratic_b = int(input("Enter b: "))
            quadratic_c = int(input("Enter c: "))
        except ValueError as error:
            print("Invalid input")
            speech_mark_index = error.args[0].index("'")
            invalid_characters = error.args[0][speech_mark_index : ]
            print(f"Invalid character/s: {invalid_characters}")

            return "invalid"

        quadratic_array = [quadratic_a, quadratic_b, quadratic_c]
        return quadratic_array

    def calculate_quadratic(self, terms) -> float:
        """ Calculates all possible roots of quadratic
        Uses quadratic formula x = (-b (+-) sqrt(b^2 - 4ac)) / 2a
        Returns: list: all roots
        """
        a = terms[0]
        b = terms[1]
        c = terms[2]
        result1 = (-b + calculator.math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
        result2 = (-b - calculator.math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
        results = [result1, result2]
        return results
        
    def output_answers(self, results) -> None:
        for result in results:
            print(result)
        
        
        
        
        