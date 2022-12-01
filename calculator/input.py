def decide_calculator_function():
    """ Takes an input from user within (1 - 4), returns input if valid
    User decides on the function of the calculator
    """    
    calculator_function = None
    print()
    print("Options:")
    print("1. Basic calculator")
    print("2. Solve quadratics")
    print("3. Calculus")
    print("4. Rearranging")
    
    while calculator_function not in ("1", "2", "3", "4"):
        calculator_function = input("> ")
    return calculator_function
    
def decide_calculus_type():
    """ Takes an input from user within (1 - 2), returns input if valid
    User decides on the type of calculus to do
    """    
    print()
    print("Options:")
    print("1. Differentiation")
    print("2. Integration")

    while calculus_type not in ("1", "2"):
        calculus_type = input("> ")
    return calculus_type
    