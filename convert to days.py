def convert_to_days():
    h = float(input("Enter a number of hours: "))
    m = float(input("Enter a number of minutes: "))
    s = float(input("Enter a number of seconds: "))
    total = get_days(h, m, s)
    print(f"The number of days is: {total}")

def get_days(h: int, m: int, s: int):
    Days = (h + (m / 60) + (s / 3600)) / 24
    return round(Days, 4)

convert_to_days()