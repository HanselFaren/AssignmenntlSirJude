import math
m = float(input("Enter the mass of the cart (in kg): "))
f = float(input("Enter the force to push the cart (in N): "))
g = 9.8
sin = f / (m * g)
degrees = math.degrees(sin)
print(f"The angle of the ramp is %0.1f degrees"%degrees)