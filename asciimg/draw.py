from PIL import Image, ImageEnhance

from .constants import ASCII_GREY_SCALE, SCALE_HEIGHT_COEFF


def img_to_ascii(filename, width, contrast=1.0):
    img = Image.open(filename)
    img_gray = img.convert('L')

    img_enhanced = enhance_contrast(img_gray, contrast)
    img_scaled = scale_img(img_enhanced, new_width=width)

    coeff = len(ASCII_GREY_SCALE) / 255
    ascii_rows = []

    for i in range(img_scaled.height):
        chars = []

        for j in range(img_scaled.width):
            index = round(img_scaled.getpixel((j, i)) * coeff)
            chars.append(get_char(index))

        ascii_rows.append(''.join(chars))

    return '\n'.join(ascii_rows)


def scale_img(img, new_width):
    aspect_ratio = img.width / img.height
    new_height = round(new_width / aspect_ratio * SCALE_HEIGHT_COEFF)

    return img.resize((new_width, new_height))


def enhance_contrast(img, contrast):
    enhancer = ImageEnhance.Contrast(img)

    return enhancer.enhance(contrast)


def get_char(index):
    min_i, max_i = 0, len(ASCII_GREY_SCALE) - 1
    i = max(min_i, min(index, max_i))

    return ASCII_GREY_SCALE[i]

