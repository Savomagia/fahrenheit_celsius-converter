inp = input("If you tell me your Fahrenheit, I'll tell your Celsius:")
try:
    fahrenheit = float(inp)
    celsius = (fahrenheit - 32) * 5/9
    print("As promised:")
    print(round(celsius, 2))
except:
    print("I mean temperature! What did you get?!")
