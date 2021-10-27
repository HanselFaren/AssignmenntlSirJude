def calc_new_height():
    w = float(input("Enter the current width: "))
    h = float(input("Enter the current height: "))
    w1 = float(input("Enter the desired width: "))
    h2 = get_new_height(w, h, w1)
    print(f"The corresponding height is: {h2}")

def get_new_height(w: int, h: int, w1: int):
    h1 = w1 * h / w
    return round(h1, 1)

calc_new_height()