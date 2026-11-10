# Check whether the temperature is below 0 degrees Celsius
# Method 1: Normal method
temperature = float(input("Enter temperature in Celsius: "))
if temperature < 0:
    print("The temperature is below 0 degrees Celsius.")

# Method 2: Function method
def check_temperature(temperature):
    if temperature < 0:
        print("The temperature is below 0 degrees Celsius.")

temperature = float(input("Enter temperature in Celsius: "))
check_temperature(temperature)
