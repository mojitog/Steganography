from PIL import Image

def get_inputs():
    """
    Welcome, selecting mode, inserting key, and data
    """
    print("Welcome to Moji's secret(!) stegnaogrpahy script")
    mode = input("Mode(E/D): ")
    key = input("Insert the key(1-100): ")
    if mode == "E":
        input("Please insert the image address: ")
    pass


def text_to_decimal(text):
    return list(map(ord, text))


key = 10
text = "Moji is really trying to be cool here!"
img = Image.open("Heath_Ledger_as_the_Joker.JPG.webp")

code_list = text_to_decimal(text)
