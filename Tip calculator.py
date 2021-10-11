s = float(input("Enter a subtotal: $"))
t = float(input("Enter tip amount (as a %): "))

subtotal = "${:,.2f}".format(s)
tip = (t/100)*s
tip1 = "${:.2f}".format(tip)
print(f"Subtotal: {subtotal}")
print(f"Tip: {tip1}")
total = s + tip
total1 = "${:,.2f}".format(total)
print(f"Total: {total1}")