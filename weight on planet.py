def calc_weight_on_planet(weight, gravity = 23.1):
    mass = weight / 9.8
    print(mass * gravity)

x = calc_weight_on_planet(120, 9.8)
y = calc_weight_on_planet(120)
z = calc_weight_on_planet(120, 23.1)