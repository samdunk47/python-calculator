def decide_calculator_function():
    calculator_function = None
    print("""
Options: 
1. Basic calculator
2. Solve quadratics
3. Calculus
4. Rearranging""")
    while calculator_function not in ("1", "2", "3", "4"):
        calculator_function = input("> ")
