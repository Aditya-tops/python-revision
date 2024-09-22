# Fahrenheit (°f) = (Temperature in degreees Celsius °F = °C×(9/5)+32

celsius_temperatures = [25,30,15,10,35]
fahrenheitlist_temperatures = list((map(lambda  c: (c * 9/5) + 32,celsius_temperatures)))
print(fahrenheitlist_temperatures)
