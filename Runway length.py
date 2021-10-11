v = float(input("Enter the plane's take off speed in m/s : "))
a = float(input("Enter the plane's acceleration in m/s**2 : "))

length = (v**2) / (2*a)

print("The minimum runway length needed for this airplane is %2.4f"%length)
