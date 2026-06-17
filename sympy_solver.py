from sympy import symbols, solveset, S

print("Welcome to the zero solver")
print()
      
x = symbols('x')

print("Enter in the form ax**n to represent squaring")
print("Enter in the form ax*n to represent multiplying")
print()

equation = input("Enter your quadratic equation: ")
print()

solutions = solveset(equation, x, domain=S.Reals)

irrational_exists = any(not s.is_rational for s in solutions)
if irrational_exists:
    decimal = input("Would you like the zeroes in decimal form?     y/n     ")
    if (decimal == "y"):
        print("Decimal solutions:", [s.evalf() for s in solutions])
        print()

complex_exists = any(not s.is_complex for s in solutions)
if complex_exists:
    complex = input("Would you like the complex zeroes?     y/n     ")
    if (complex == "y"):
        complex_solutions = solveset(equation, x, domain=S.Complexes)
        print("Complex solutions:", list(complex_solutions))
        print()
