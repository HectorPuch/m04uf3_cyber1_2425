import urllib.request, json

def show_weather(city_name, latitude, longitude):
    
    url_weather = "https://api.open-meteo.com/v1/forecast?latitude=" + str(latitude) + "&longitude=" + str(longitude) + "&current=temperature_2m,wind_speed_10m,relative_humidity_2m"

    with urllib.request.urlopen(url_weather) as data:
        parsed = json.load(data)

    print("--- The weather in " + str(city_name) + " ---")
    print("Temperature:", parsed["current"]["temperature_2m"])
    print("Wind speed:", parsed["current"]["wind_speed_10m"])
    print("Relative humidity:", parsed["current"]["relative_humidity_2m"])

def show_menu_weather_app():

    option_menu = -1

    while option_menu != 0:
        print("--- Weather App Menu ---")
        print("1. Barcelona")
        print("2. Madrid")
        print("3. Berlin")
        print("4. London")
        print("5. Paris")
        print("6. New York")
        print("0. Exit")

        option_menu = input("Choose an option (0-6): ")

        if option_menu.isdigit():
            option_menu = int(option_menu)
            match option_menu:
                case 0:
                    print("Goodbye.")
                case 1:
                    show_weather("Barcelona", 41.3888, 2.159)
                case 2:
                    show_weather("Madrid", 40.4165, -3.7026)
                case 3:
                    show_weather("Berlin", 52.5244, 13.4105)
                case 4:
                    show_weather("London", 51.5085, -0.1257)
                case 5:
                    show_weather("Paris", 48.8534, 2.3488)
                case 6:
                    show_weather("New York", 40.7143, -74.006)
                case _:
                    print("Please, enter a number between 0 and 6.")
        else:
            print("Error: You must enter a valid number.")

show_menu_weather_app()

