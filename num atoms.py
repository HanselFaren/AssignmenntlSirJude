def num_atoms(grams, Aweight = 196.97):
    atomic = grams / Aweight
    print(atomic * 6.0222 * (10**23))

x = num_atoms(10)
y = num_atoms(10, 12.001)
z = num_atoms(10, 1.008)