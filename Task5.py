def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

# Example conversions
celsius = 60
fahrenheit = 45

print(f"{celsius}°C is {celsius_to_fahrenheit(celsius):.0f} in Fahrenheit")
print(f"{fahrenheit}°F is {fahrenheit_to_celsius(fahrenheit):.0f} in Celsius")
