import requests
from tkinter import *
from PIL import Image, ImageTk
import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env

API_KEY = os.getenv("API_KEY")

FONT_MAIN = ("Poppins", 12)
FONT_TITLE = ("Poppins", 16, "bold")

def get_weather():
    city = city_entry.get()
    if not city:
        result_label.config(text="Please enter a city name!", foreground="red", background="#FFDFDF", padx=10, pady=5, font=("Poppins", 11))
        return
    
     # Show loading & disable button
    result_label.config(text="Loading...", foreground="black", background=root.cget("bg"))
    search_btn.config(state="disabled")
    root.update_idletasks()
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data.get('cod') != 200:
            result_label.config(text="City not found!", foreground="red", background="#FFDFDF", padx=10, pady=5, font=("Poppins", 11))
            search_btn.config(state="normal")
            return
        
        city_name = data['name']
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']

        result = f"City: {city_name}\nTemperature: {temperature}°C\nWeather: {weather_description.capitalize()}"
        result_label.config(text= result, background="#DFFFD6", foreground="black", padx=10, pady=5, font=("Poppins", 11))
        city_entry.delete(0, END)
        root.focus()

    except Exception as e:
        result_label.config(text="Error fetching data!", foreground="red", background="#FFDFDF", padx=10, pady=5, font=("Poppins", 11))
        search_btn.config(state="normal")
        return
    
    # Re-enable button after work is done
    search_btn.config(state="normal")

root = Tk()
root.title("Weather App")
root.geometry("450x480")
root.resizable(True, True)

# Container frame for better layout
container = Frame(root, bg="#F2F2F2", relief="solid")
container.pack(pady=20, padx=20)

try:
    img = Image.open("weather.png")  # Put a weather.png image in the same folder
    img = img.resize((100, 100))
    icon = ImageTk.PhotoImage(img)
    icon_label = Label(container, image=icon)
    icon_label.pack(pady=10)
except:
    pass

# Title
Label(container, text="Enter City Name:", font=("Poppins", 14)).pack(pady=5)

# Input field
city_entry = Entry(container, font=("Poppins", 12), justify='center', foreground="#9f9f9f")
city_entry.insert(0, "City Name")
city_entry.pack(pady=5)

def on_focus_in(event):
    if city_entry.get() == "City Name":
        city_entry.delete(0, END)
        city_entry.config(foreground="black")

city_entry.bind("<FocusIn>", on_focus_in)

def on_focus_out(event):
    if city_entry.get() == "":
        city_entry.insert(0, "City Name")
        city_entry.config(foreground="#9f9f9f")

city_entry.bind("<FocusOut>", on_focus_out)

# Button
search_btn = Button(container, text="Get Weather", font=FONT_MAIN, bg="#4CAF50", fg="white", activebackground="#45A049", command=get_weather)
search_btn.pack(pady=10)

# Result display
result_label = Label(container, text="", font=("Arial", 12), justify="center")
result_label.pack(pady=10)

Label(container, text="Made by Robiul Islam", font=("Poppins", 8), fg="gray").pack(side="bottom", pady=5)


# Run app
root.mainloop()