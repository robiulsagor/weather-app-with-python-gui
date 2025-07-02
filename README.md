
##🌤️ Tkinter Weather App

A simple desktop GUI application built using Python and Tkinter to fetch real-time weather data from the OpenWeatherMap API.  
It's clean, responsive, and beginner-friendly — great for learning or showcasing basic API integration with GUI logic.

------------------------------------------------------------

#📸 Preview

[weather.png]

------------------------------------------------------------

#🚀 Features

- Real-time weather fetch by city name
- Clean GUI layout using Tkinter
- Input validation and error messages
- Loading indicator during fetch
- Styled UI using custom fonts, colors, and borders
- Uses Pillow for image handling

------------------------------------------------------------

#🛠️ Technologies Used

- Python 3.x
- Tkinter (GUI)
- requests (API call)
- Pillow (Image support)
- OpenWeatherMap API

------------------------------------------------------------

#📦 Installation & Setup

1. Clone the repository

   git clone https://github.com/YOUR_USERNAME/weather-app-python.git
   cd weather-app-python

2. Install required packages

   pip install requests pillow

3. Add your OpenWeatherMap API key

   Edit main.py and replace this line:
   API_KEY = "YOUR_API_KEY_HERE"

4. Run the app

   python main.py

------------------------------------------------------------

#🖼️ Screenshots

[screenshot.png]

------------------------------------------------------------

#📝 How It Works

1. User enters a city name.
2. On button click, app fetches live weather data using OpenWeatherMap API.
3. Weather info (temperature, description) is displayed inside the GUI.

------------------------------------------------------------

#📌 TODO / Future Improvements

- Add animated spinner instead of text-based loading
- Support for saving weather history
- Add location auto-detection using IP
- Multi-language support (English, Bengali, etc.)
- Dark mode toggle

------------------------------------------------------------

#📄 License

This project is open-source and free to use under the MIT license.

------------------------------------------------------------

#🙌 Acknowledgements

- OpenWeatherMap for the weather API
- Pillow for image support
- You — for visiting this repo! ❤️
