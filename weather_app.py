
import streamlit as st
import requests

def get_weather(city_name):
    api_key = "Enter API KEY"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key
    response = requests.get(complete_url)

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        temperature = main['temp'] - 273.15  # Convert from Kelvin to Celsius
        humidity = main['humidity']
        description = weather['description']
        return {
            "temperature": temperature,
            "humidity": humidity,
            "description": description
        }
    else:
        return None

st.title("Real-Time Weather App")
city_name = st.text_input("Enter city name", "")

if city_name:
    weather_data = get_weather(city_name)
    if weather_data:
        st.write(f"### Weather in {city_name.capitalize()}")
        st.write(f"**Temperature:** {weather_data['temperature']:.2f}°C")
        st.write(f"**Humidity:** {weather_data['humidity']}%")
        st.write(f"**Description:** {weather_data['description']}")
    else:
        st.write("City not found or error fetching data.")
