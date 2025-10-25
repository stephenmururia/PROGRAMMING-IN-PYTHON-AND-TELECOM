def temperature_converter():
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    choice = input("Choose an option (1 or 2): ")

    if choice == "1":
        f = float(input("Enter temperature in Fahrenheit: "))
        c = (f - 32) * 5 / 9
        print(f"{f}°F = {c:.2f}°C")
    elif choice == "2":
        c = float(input("Enter temperature in Celsius: "))
        f = (c * 9 / 5) + 32
        print(f"{c}°C = {f:.2f}°F")
    else:
        print("Invalid choice.")

temperature_converter()
