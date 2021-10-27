e1 = float(input("Enter length of edge1: "))
e2 = float(input("Enter length of edge2: "))
e3 = float(input("Enter length of edge3: "))

final = e1 + e2 + e3
if e1 + e2 > e3:
    if e2 + e3 > e1:
        if e1 + e3 > e2:
            print(f"The perimeter is {final}")
else:
    print("Perimeter cannot be calculated: the input is invalid")