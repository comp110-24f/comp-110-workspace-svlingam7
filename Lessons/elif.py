def get_weather_report() -> str:
    weather: str = input("What is the weather:")

    if weather == "rainy" or weather == "cold":
        print("Bring a Jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize the weather")

    return weather


get_weather_report()
