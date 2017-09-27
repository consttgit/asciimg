from PIL import Image

from .constants import ASCII_GREY_SCALE, SCALE_HEIGHT_COEFF


def scale_img(img, new_width):
    aspect_ratio = img.width / img.height
    new_height = round(new_width / aspect_ratio * SCALE_HEIGHT_COEFF)
    return img.resize((new_width, new_height))


def get_char(index):
    min_i, max_i = 0, len(ASCII_GREY_SCALE) - 1
    i = max(min_i, min(index, max_i))
    return ASCII_GREY_SCALE[i]


def img_to_ascii(filename, width):
    img = Image.open(filename)
    img_gray = img.convert('L')
    img_scaled = scale_img(img_gray, new_width=width)

    coeff = len(ASCII_GREY_SCALE) / 255
    ascii_chars = []

    for i in range(img_scaled.height):
        for j in range(img_scaled.width):
            index = round(img_scaled.getpixel((j, i)) * coeff)
            ascii_chars.append(get_char(index))

        ascii_chars.append('\n')

    return ''.join(ascii_chars)

