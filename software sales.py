p = float(input("Enter the number of packages purchased: "))
if p < 10:
    a = 99*p*0
    total = 99*p-a
    a1 = "${:,.2f}".format(a)
    print(f"Discount Amount @ 0% : {a1}")
elif 10 <= p <=19:
    a = 99*p*(1/10)
    total = 99 * p - a
    a1 = "${:,.2f}".format(a)
    print(f"Discount Amount @ 10% : {a1}")
elif 20 <= p <= 49:
    a = 99*p*(1/5)
    total = 99 * p - a
    a1 = "${:,.2f}".format(a)
    print(f"Discount Amount @ 20% : {a1}")
elif 50 <= p <= 99:
    a = 99 * p * (3/10)
    total = 99 * p - a
    a1 = "${:,.2f}".format(a)
    print(f"Discount Amount @ 30% : {a1}")
else:
    a = 99 * p * (2/5)
    a1 = "${:,.2f}".format(a)
    total = 99 * p - a
    print(f"Discount Amount @ 40% : {a1}")
total1 = "${:,.2f}".format(total)
print(f"Total Amount = {total1}")