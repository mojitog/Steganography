from PIL import Image
from random import randint
import pickle

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


def create_key(x, y, n):
    tuples_list = []
    i = 0
    while i < n:
        rand_x = randint(0,x-1)
        rand_y = randint(0,y-1)
        if (rand_x, rand_y) not in tuples_list:
            tuples_list.append((rand_x, rand_y))
            i += 1
    return tuples_list


def save_key(key):
    with open('key', 'wb') as key_file:
        pickle.dump(key, key_file)


def encrypt():
    text = "Moji is really trying to be cool here!"
    code_list = text_to_decimal(text)

    img = Image.open("Heath_Ledger_as_the_Joker.JPG.webp")
    img_width, img_height = img.size
    key = create_key(img_width, img_height, len(code_list))
    save_key(key)

    for pixel in key:
        pixel_rgb = img.getpixel(pixel)
        index = key.index(pixel)
        img.putpixel(pixel, (code_list[index], pixel_rgb[1], pixel_rgb[2]))
        #img.putpixel(pixel, (0, 0, 0))

    img.show()
    img.save("new_image.png")


def load_key():
    with open('key', 'rb') as key_file:
        return pickle.load(key_file)
    

def code_to_text(code):
    word_list = list(map(chr, code))
    delimiter = ""
    return delimiter.join(word_list)

def decrypt():
    img = Image.open("new_image.png")
    key = load_key()
    code = []
    
    for pixel in key:
        num = img.getpixel(pixel)[0]
        code.append(num)

    text = code_to_text(code)

    print(text)