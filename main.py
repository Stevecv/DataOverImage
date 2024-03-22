from math import floor

from PIL import Image


def encode(text, image_name):
    im = Image.open(image_name)
    width, height = im.size

    total_pixels = width * height
    text_length = len(text)
    pixel_spacing = floor(total_pixels / text_length)

    leftover_pixel_spacing = pixel_spacing
    if pixel_spacing > 765:
        pixel_spacing = 765
    pixel_spacing_r = leftover_pixel_spacing
    pixel_spacing_g = leftover_pixel_spacing-255
    pixel_spacing_b = leftover_pixel_spacing-510

    if pixel_spacing_g < 0:
        pixel_spacing_g = 0
    if pixel_spacing_b < 0:
        pixel_spacing_b = 0

    if pixel_spacing_r >= 255:
        pixel_spacing_r = 255
    if pixel_spacing_g >= 255:
        pixel_spacing_g = 255
    if pixel_spacing_b >= 255:
        pixel_spacing_b = 255

    text_length = len(text)
    len_r = text_length
    len_g = text_length - 255
    len_b = text_length - 510

    im.putpixel((0, 0), (pixel_spacing_r, pixel_spacing_g, pixel_spacing_b))
    meta_color = im.getpixel((0, 0))

    text_array = list(text)
    pixel_index = 0
    for letter in text_array:
        pixel_index += pixel_spacing
        y = floor(pixel_index / width)
        x = floor(pixel_index % width)

        color = im.getpixel((x, y))
        im.putpixel((x, y), (color[0], color[1], ord(letter)))

    start_index = (len(text_array)+1) * pixel_spacing
    for index in range(start_index, total_pixels):
        if index % pixel_spacing == 0:
            y = floor(index / width)
            x = floor(index % width)

            pixel = im.getpixel((x, y))
            im.putpixel((x, y), (pixel[0], pixel[1], 0))

    return im


def decode(image_name):
    im = Image.open(image_name)
    meta_color = im.getpixel((0, 0))
    pixel_spacing = meta_color[0] + meta_color[1] + meta_color[2]
    width, height = im.size

    possible_pixels = width*height

    return_string = ""
    for pixel_index in range(1, possible_pixels):
        if pixel_index % pixel_spacing == 0:
            y = floor(pixel_index / width)
            x = floor(pixel_index % width)

            pixel = im.getpixel((x, y))[2]
            ch = chr(pixel)
            if ch.isprintable():
                return_string += ch

    return return_string


def print_menu():
    print("Would you like to")
    print("1. Encode an image")
    print("2. Decode an image")
    print("3. Exit")
    print("")
    choice = input(" > ")
    print("")
    print("")
    print("Please enter a file or filepath")
    filePath = input(" > ")

    if choice.lower() == "1" or choice.lower() == "encode" or choice.lower() == "e":
        print("")
        print("")
        print("Please enter your text to encode")
        text = input(" > ")
        try:
            im = encode(text, filePath)
            print("")
            print("")
            print("File encoded successfully! Please enter a name to save the image under")
            save_name = input(" > ")
            if "." not in save_name:
                save_name += ".png"

            im.save(".\\" + save_name)
            print("Saved image under " + save_name)
        except:
            print("An error has occurred, does that file exist?")

    elif choice.lower() == "2" or choice.lower() == "decode" or choice.lower() == "d":
        try:
            print(decode(filePath))
        except:
            print("An error has occurred, does that file exist?")

    elif choice.lower() == "3" or choice.lower() == "exit" or choice.lower() == "ex":
        return False

    else:
        print("Invalid input!")
        return True

    print("")
    print("")
    print("")
    print("")
    print("")

    return True


should_run = True
while should_run:
    should_run = print_menu()