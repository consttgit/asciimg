#!/usr/bin/env python3
"""asciimg - convert image into ASCII text.
"""
import argparse
from PIL import Image


ASCII_GREY_SCALE = '$@B8#%&WMX0QOLZ|?+;:~-"^\'_,. '


def scale_img(img, new_width):
    width, height  = img.size
    aspect_ratio = width / height
    new_height = round(new_width / aspect_ratio * 0.5)
    return img.resize((new_width, new_height))


def get_char(index):
    min_i = 0
    max_i = len(ASCII_GREY_SCALE) - 1
    if index < min_i:
        return ASCII_GREY_SCALE[min_i]
    elif index > max_i:
        return ASCII_GREY_SCALE[max_i]
    else:
        return ASCII_GREY_SCALE[index]
    

def img_to_ascii(img):
    width, height = img.size
    coeff = len(ASCII_GREY_SCALE) / 255
    ascii_chars = []
    for i in range(height):
        for j in range(width):
            index = round(img.getpixel((j, i)) * coeff)
            ascii_chars.append(get_char(index))
        ascii_chars.append('\n')
    return ''.join(ascii_chars)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('image', help='image file')
    parser.add_argument('-w', '--width', type=int, default=79,
                        help='ascii width (char)')
    args = parser.parse_args()

    try:
        img = Image.open(args.image)
    except FileNotFoundError as e:
        print('Error:', e)
        return

    img_gray = scale_img(img, new_width=args.width).convert('L')
    img_ascii = img_to_ascii(img_gray)

    print(img_ascii)


if __name__ == '__main__':
    main()
