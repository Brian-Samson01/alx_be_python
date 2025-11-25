#Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius.

    Args:
        fahrenheit (float): Temperature in Fahrenheit.

    Returns:
        float: Temperature in Celsius.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit.

    Args:
        celsius (float): Temperature in Celsius.

    Returns:
        float: Temperature in Fahrenheit.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    # Prompt user for temperature
    temp_input = input("Enter the temperature to convert: ")

    #validate numeric input
    try:
        temp_value = float(temp_input)
    except ValueError:
        raise ValueError("Invalid input. Please enter a numeric value.")
    
    # prompt for unit
    unit = input("Is this in Fahrenheit or Celsius? (F/C): ").strip().upper()
    if unit == 'F':
        celsius = fahrenheit_to_celsius(temp_value)
        print(f"{temp_value}°F is {celsius:.2f}°C")
    elif unit == 'C':
        fahrenheit = celsius_to_fahrenheit(temp_value)
        print(f"{temp_value}°C is {fahrenheit:.2f}°F")
    else:
        raise ValueError("Invalid unit. Please enter 'F' for Fahrenheit or 'C' for Celsius.")


if __name__ == "__main__":
    main()