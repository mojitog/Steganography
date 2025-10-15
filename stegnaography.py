from PIL import Image
from random import randint

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


def random_tuples(x, y, n):
    tuples_list = []
    i = 0
    while i < n:
        rand_x = randint(0,x)
        rand_y = randint(0,y)
        if (rand_x, rand_y) not in tuples_list:
            tuples_list.append((rand_x, rand_y))
            i += 1
    return tuples_list


key = 10
text = "Moji is really trying to be cool here!"
code_list = text_to_decimal(text)

img = Image.open("Heath_Ledger_as_the_Joker.JPG.webp")
img_width, img_height = img.size

print(random_tuples(img_width, img_height, len(code_list)))