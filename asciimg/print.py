import os
import math
import shutil

import numpy as np


def img_print(img_ascii, filename, width, height):
    dirname = os.path.splitext(filename)[0]

    if os.path.exists(dirname):
        shutil.rmtree(dirname)

    os.mkdir(dirname)
    pages = page_generator(img_ascii, width, height)

    for i, page in enumerate(pages):
        fname = os.path.join(dirname, 'page_{}.txt'.format(i + 1))

        with open(fname, 'w') as f:
            f.write(page)


def page_generator(img_ascii, width, height):
    arr = txt_to_arr(img_ascii)

    n_width_pages = math.ceil(arr.shape[1] / width)
    n_height_pages = math.ceil(arr.shape[0] / height)

    for i in range(n_width_pages):
        for j in range(n_height_pages):
            h_start = j * height
            h_end = h_start + height

            w_start = i * width
            w_end = w_start + width

            page_arr = arr[h_start:h_end, w_start:w_end]
            page_txt = arr_to_txt(page_arr)

            yield page_txt


def txt_to_arr(txt):
    txt_arr = []

    for line in txt[:-1].split('\n'):
        txt_arr.append([char for char in line])

    return np.array(txt_arr)


def arr_to_txt(arr):
    txt_lines = []

    for row in arr:
        txt_lines.append(''.join(row))

    return '\n'.join(txt_lines)

