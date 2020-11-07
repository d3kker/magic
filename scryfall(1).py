import requests
import json
from tkinter import filedialog
#from tkinter import askopenfilename 
import tkinter
import pandas as pd





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

            #img = Image.open(urlopen(image_border_crop))
            #img.show()
            write_css_file(image_large)
        except:
            print("Could not find card")


if __name__ == "__main__":



    window = tkinter.Tk()
    window.title("OBS")
    window.geometry('1100x550')

    label = tkinter.Label(window, text="Card Name").place(x = 25, y = 250)

    entry = tkinter.Entry(window)
    entry.place(x = 100, y = 250)

    def callback(event="<Button>"):
        # print(entry.get())
        find_card_image(entry.get())


    def specific_callback(card, event="<Button>"):
        find_card_image(card)


    def callback_for_button():
        print("Button clicked!")


    def open1():
        window.filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("txt files", ".txt"),("all files", ".*"))) 
        #filename = askopenfilename()
    
    entry.bind("<Return>", callback)

    button = tkinter.Button(window, text="Click Me!", command=callback)
    button.place(x = 230, y = 246)
    print(button["text"])

    button2 = tkinter.Button(window, text="Open File", command=open1, )
    button2.place(x = 1000, y = 246)
    





    # df is a pandas DataFrame, like a table
    df = pd.read_csv("2face2.txt", sep=";", header=None)
    list_of_cards = df[0].values
    print(df)
    #y0 = 0
    row_index = 0
    for index, card in enumerate(list_of_cards):
        button = tkinter.Button(window, text=card, command=lambda x=card: find_card_image(x), height = 1, width = 30)
        button.grid(row=row_index, column=index%5)
        if (index + 1) % 10 == 0:
            row_index = row_index + 1

       
    window.mainloop()




