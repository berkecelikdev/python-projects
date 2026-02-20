import requests

class WeatherApp:
    def __init__(self, api_key):
        # Getting the API key when the class is initialized
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city_name):
        # Parameters to send to API
        params = {
            "q" : city_name,
            "appid" : self.api_key,
            "units" : "metric", # For Celsius
            "lang" : "en" # English description
        }

        try:
            # Fetching data from the internet (GET request)
            response = requests.get(self.base_url, params = params)
            response.raise_for_status() # Catches HTTP errors

            # Converting the received data to JSON format
            data = response.json()

            # Extracting the necessary parts from the dictionary
            temperature = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            description = data["weather"][0]["description"]

            # Printing the results neatly
            print(f"--- {city_name.upper()} WEATHER ---")
            print(f"Temperature: {temperature}C")
            print(f"Feels Like: {feels_like}C")
            print(f"Condition: {description.title()}")
            print("-" * 30)

        except requests.exceptions.HTTPError:
            print(f"Error: City '{city_name}' not found or invalid API key.")
        except requests.exceptions.RequestException:
            print("Error: Please check your internet connection.")

# The main block where we run the program
if __name__ == "__main__":
    # Your API key
    my_api_key = "YOUR_OWN_KEY "

    # Creating an object from our class
    app = WeatherApp(my_api_key)

    city_from_user = input("Please enter the city name: ")

    app.get_weather(city_from_user)
    



