# Check whether a vehicle's speed exceeds a specified speed limit

speed = float(input("Enter the vehicle's speed (km/h): "))
limit = float(input("Enter the speed limit (km/h): "))

if speed > limit:
    print("The vehicle is over the speed limit.")
else:
    print("The vehicle is within the speed limit.")
