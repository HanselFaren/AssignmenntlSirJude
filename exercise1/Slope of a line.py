x1 = float(input("Enter the x-coordinate for point1 : "))
y1 = float(input("Enter the y-coordinate for point1 : "))
x2 = float(input("Enter the x-coordinate for point2 : "))
y2 = float(input("Enter the y-coordinate for point2 : "))

slope = (y2-y1) / (x2-x1)
print(f"The slope for the line that connects two points ({x1}, {y1}) and ({x2, y2}) is %2.5f"%(slope))