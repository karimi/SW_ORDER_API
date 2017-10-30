import json
import webbrowser
from shapeways.client import Client
from credentials import Credentials

chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

client = Client(
    Credentials["Consumer_Key"],
    Credentials["Consumer_Secret"],
    callback_url="http://localhost:3000/callback"
)

url=client.connect()
print url

#webbrowser.get(chrome_path).open(url,new=2)
