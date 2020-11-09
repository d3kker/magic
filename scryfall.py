import json
import pandas as pd
from PIL import Image
import requests
import shutil
import tkinter
from tkinter import filedialog
from urllib.request import urlopen


def write_css_file(url):
    """
    Write a .css linking to the image URL.
    The .css file is read by OBS and displays the card image.
    """
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
    if card == "":
        write_css_file("")
    else:
        try:
            response = requests.get("https://api.scryfall.com/cards/named?fuzzy=" + card)

            parsed = json.loads(response.text)
           #print(json.dumps(parsed, indent=4))

            #image_normal = parsed["image_uris"]["normal"]
            image_large = parsed["image_uris"]["large"]
            #image_border_crop = parsed["image_uris"]["border_crop"]

            img = Image.open(urlopen(image_large))
            img.show()
            write_css_file(image_large)
        except:
            print("Could not find card")


if __name__ == "__main__":
    window = tkinter.Tk()
    window.title("OBS")

    window_x = 1100
    window_y = 750

    window.geometry(f"{window_x}x{window_y}")

    label_x = 25
    label_y = 0.8 * window_y

    label = tkinter.Label(window, text="Card search").place(x=label_x, y=label_y)

    entry = tkinter.Entry(window)
    entry.place(x=label_x+100, y=label_y)

    def callback(event="<Button>"):
        find_card_image(entry.get())

    # Save each deck in this list in order to destroy them when a new deck is loaded with open_card_deck_file()
    list_of_buttons = []

    def open_card_deck_file():
        """
        Open file browser window, select deck file and display each card as a button.
        Will destroy buttons loaded from previous deck files.
        """
        for button in list_of_buttons:
            button.destroy()
        # Empty the list
        list_of_buttons.clear()

        # Card deck file selection window
        card_deck_file = filedialog.askopenfilename(title="Select A File", filetypes=(("txt files", ".txt"),("all files", ".*")))

        # df is a pandas DataFrame, like a table
        df = pd.read_csv(card_deck_file, sep=";", header=None)
        list_of_cards = df[0].values

        row_index = 0
        number_of_columns = 5

        for index, card in enumerate(list_of_cards):
            button = tkinter.Button(window, text=card, command=lambda x=card: find_card_image(x), height=1, width=30)
            button.grid(row=row_index, column=index%number_of_columns)
            list_of_buttons.append(button)
            if (index + 1) % number_of_columns == 0:
                row_index = row_index + 1


    entry.bind("<Return>", callback)

    button_search_card = tkinter.Button(window, text="Search", command=callback)
    button_search_card.place(x=label_x+230, y=label_y)

    button_load_deck = tkinter.Button(window, text="Load deck file", command=open_card_deck_file)
    button_load_deck.place(x=25, y=0.9*window_y)

    card_deck_file = open_card_deck_file()

    window.mainloop()