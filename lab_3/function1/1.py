def to_ounces(grams):
    ounces = grams / 28.3496231
    return ounces

grams = int(input("Enter the weight in grams: "))

print(to_ounces(grams), "ounces")

