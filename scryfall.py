import requests
import json
import webbrowser
from urllib.request import urlopen
from PIL import Image

def write_css_file(url):
    with open("background.css", "w") as css_file:
        css_file.write("body")
        css_file.write("\n")
        css_file.write("{")
        css_file.write("\n")
        css_file.write(f"background-image: url(\"{url}\");")
        css_file.write("\n")
        css_file.write("background-repeat: no-repeat;")
        css_file.write("\n")
        css_file.write("background-color: #cccccc;")
        css_file.write("\n")
        css_file.write("}")


while True:
    card = input("Enter card name:")

    if card == "empty":
        write_css_file("")
    else:
        response = requests.get("https://api.scryfall.com/cards/named?fuzzy=" + card)

        parsed = json.loads(response.text)
        #print(json.dumps(parsed, indent=4))

        image_normal = parsed["image_uris"]["normal"]
        image_large = parsed["image_uris"]["large"]
        image_border_crop = parsed["image_uris"]["border_crop"]


        #webbrowser.open(image_normal, new=1)
        #img = Image.open(urlopen(image_border_crop))
        #img.show()
        write_css_file(image_large)

