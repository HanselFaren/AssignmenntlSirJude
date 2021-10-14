t = float(input("Enter the temperature in Fahrenheit: "))
while True:
        if t < -58 or t > 41:
                print("Temperature must be between -58F and 41F")
                t = float(input("Please re-enter the temperature in Fahrenheit: "))
        else:
                break
s = float(input("Enter the wind speed miles per hour: "))
while True:
        if s < 2:
                print("Speed must be greater than or equal to 2")
                s = float(input("Please re-enter the wind speed miles per hour: "))
        else:
                break
t1 = 35.74 + 0.6215*t - 35.75*(s**0.16) + 0.4275*t*(s**0.16)
print("The wind chill index is %0.3f"%t1)