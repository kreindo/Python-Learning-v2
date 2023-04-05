import sys
import requests
import os
import json
from dotenv import load_dotenv
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


load_dotenv()
url = "https://api.openweathermap.org/data/2.5/weather"
api_key = os.getenv("API_KEY")
params = {
    "q"     : "Makassar",
    "appid" : "5e21d363cdc4f29f6c0f2d95799d8f84",
    "units" : "metric"
}

print(os.getenv("API_KEY"))

response = requests.get(url, params=params)

if response.status_code == 200:
    data = json.loads(response.text)
    print(data)
else:
    print(json.loads(response.text))

app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle('Aplikasi Ahmad')

label = QLabel(window)
label.setText(json.dumps(response.text))
label.move(50, 50)

window.setGeometry(100, 100, 200, 100)
window.show()

sys.exit(app.exec_())