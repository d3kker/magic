import requests
import json
from urllib.request import urlopen
from PIL import Image
import tkinter

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
        css_file.write("}")


def find_card_image(card):
    if card == "empty":
        write_css_file("")
    else:
        try:
            response = requests.get("https://api.scryfall.com/cards/named?fuzzy=" + card)

            parsed = json.loads(response.text)
            #print(json.dumps(parsed, indent=4))

            image_normal = parsed["image_uris"]["normal"]
            image_large = parsed["image_uris"]["large"]
            image_border_crop = parsed["image_uris"]["border_crop"]

            img = Image.open(urlopen(image_border_crop))
            img.show()
            write_css_file(image_large)
        except:
            print("Could not find card")


if __name__ == "__main__":



    window = tkinter.Tk()
    window.title("OBS")
    window.geometry('550x300')

    label = tkinter.Label(window, text="Card Name").place(x = 25, y = 15)

    entry = tkinter.Entry(window)
    entry.place(x = 100, y = 15)

    def callback(event="<Button>"):
        print(entry.get())
        find_card_image(entry.get())


    def specific_callback(card, event="<Button>"):
        find_card_image(card)

    def callback_for_button(card):
        print("Button clicked!")
        find_card_image(card)

    entry.bind("<Return>", callback)

    button = tkinter.Button(window, text="Click Me!", command=callback).place(x = 230, y = 11)
    button_2 = tkinter.Button(window, text="Anger", command=callback_for_button("Anger")).place(x = 230, y = 51)

    list_of_cards = ["Anger", "Opt", "Biovisionary", "Rebuild"]

    """
    y0 = 0
    for card in list_of_cards:
        tkinter.Button(window, text=card, command=specific_callback(card, event="<Button>")).place(x = 230, y = 51 + y0)
        y0 = y0 + 40
    """

    window.mainloop()




