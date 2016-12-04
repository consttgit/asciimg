#!/usr/bin/env python3
"""asciimg - convert image into ASCII text.
"""
import sys
import argparse
from PIL import Image


ASCII_GREY_SCALE = '$@B8#%&WMX0QOLZ|?+;:~-"^\'_,. '


def get_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('image', help='image file')
    parser.add_argument('-w', '--width', type=int, default=79,
                        help='ascii width (char)')
    return parser.parse_args()


def scale_img(img, new_width):
    aspect_ratio = img.width / img.height
    new_height = round(new_width / aspect_ratio * 0.5)
    return img.resize((new_width, new_height))


def get_char(index):
    min_i, max_i = 0, len(ASCII_GREY_SCALE) - 1
    i = max(min_i, min(index, max_i))
    char = ASCII_GREY_SCALE[i]
    return char
    

def img_to_ascii(img):
    coeff = len(ASCII_GREY_SCALE) / 255
    ascii_chars = []
    for i in range(img.height):
        for j in range(img.width):
            index = round(img.getpixel((j, i)) * coeff)
            ascii_chars.append(get_char(index))
        ascii_chars.append('\n')
    return ''.join(ascii_chars)


def main():
    args = get_args()

    try:
        img = Image.open(args.image)
    except FileNotFoundError as e:
        print('Error:', e)
        sys.exit(-1)

    img_gray = img.convert('L')
    img_scaled = scale_img(img_gray, new_width=args.width)
    img_ascii = img_to_ascii(img_scaled)

    print(img_ascii)


if __name__ == '__main__':
    main()


