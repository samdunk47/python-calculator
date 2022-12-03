def decide_calculator_function():
    """ Takes an input from user within (1 - 4), returns input if valid
    User decides on the function of the calculator
    Returns: str: number corresponding to the function of the calculator
    """    
    calculator_function = None
    print()
    print("Options:")
    print("1. Basic calculator")
    print("2. Solve quadratics")
    print("3. Calculus")
    print("4. Rearranging")
    print("5. Surd simplification")
    
    while calculator_function not in ("1", "2", "3", "4", "5"):
        calculator_function = input("> ")
        
    return calculator_function
    
def decide_calculus_type():
    """ Takes an input from user within (1 - 2), returns input if valid
    User decides on the type of calculus to do
    Returns: str: number corresponding to the calculus function
    """    
    calculus_type = None
    print()
    print("Options:")
    print("1. Differentiation")
    print("2. Integration")

    while calculus_type not in ("1", "2"):
        calculus_type = input("> ")
        
    return calculus_type
    