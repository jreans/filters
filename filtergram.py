from filters import *

def main():
    filename = input("Pick an image: ")
    image = load_img(filename)
    filtername = input("Pick a filter: ")
    if filtername == "inverse rainbow":
        new_image = invrainbowfilter(image)
    elif filtername == "rainbow":
        new_image = rainbowfilter(image)
    elif filtername == "obama":
        new_image = obamicon(image)
    save_img(new_image,"recolored.jpg")

main()
