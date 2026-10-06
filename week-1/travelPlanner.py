destination = input("enter your destination: ")
distance = float(input("enter distance in kilometers: "))
speed = float(input("enter speed in km/h: "))

time = distance / speed

print(f"Destination: {destination}\nDistance: {distance} km\nAverage Speed: {speed} km/h\n\nEstimated Travel Time: {time} hours")