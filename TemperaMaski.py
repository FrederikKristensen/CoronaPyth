from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

white True:
    temp = sense.get_temperature()
    if temp >= 37 and temp < 38:
        print("Normal Temperature: " + str(temp))
    elif temp >= 38 and temp < 45:
        print("High Temperature: " + str(temp))
    elif temp < 36 or temp > 45:
        print("Invalid Temperature: " + str(temp))