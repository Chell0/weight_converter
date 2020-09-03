# Ask user their weight
weight = int(input('Weight: '))
# Ask  user to choose unit
unit = input('(L)bs or (K)gs: ')

if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")
