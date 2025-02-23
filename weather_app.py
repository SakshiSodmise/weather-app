
import streamlit as st
import requests

def get_weather(city_name):
    api_key = "Enter API Key"
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

st.title("🌞 Real-Time Weather App ⛅")
st.markdown("<h3 style='color:skyblue;'>Check the weather in your city! ☂️</h3>", unsafe_allow_html=True)

city_name = st.text_input("Enter city name 🏙️", "")

if city_name:
    weather_data = get_weather(city_name)
    if weather_data:
        st.markdown(f"<h3 style='color:blue;'>Weather in {city_name.capitalize()} 🌦️</h3>", unsafe_allow_html=True)
        st.markdown(f"<h4 style='color:orange;'>🌡️ Temperature:</h4> <p style='font-size:18px;'>{weather_data['temperature']:.2f}°C</p>", unsafe_allow_html=True)
        st.markdown(f"<h4 style='color:green;'>💧 Humidity:</h4> <p style='font-size:18px;'>{weather_data['humidity']}%</p>", unsafe_allow_html=True)
        st.markdown(f"<h4 style='color:purple;'>🌈 Description:</h4> <p style='font-size:18px;'>{weather_data['description'].capitalize()}</p>", unsafe_allow_html=True)
    else:
        st.markdown("<h3 style='color:red;'>City not found or error fetching data. 😓</h3>", unsafe_allow_html=True)
