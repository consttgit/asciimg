#!/usr/bin/env python3
"""asciimg - convert image into ASCII text.
"""
import sys
import argparse

import asciimg
from asciimg.draw import img_to_ascii
from asciimg.print import img_print


def get_args():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument('image', help='image file')
    parser.add_argument('-w', '--width', type=int, default=79,
                        help='ascii width (char)')
    parser.add_argument('-c', '--contrast', type=float, default=1.0,
                        help='contrast coefficient (min 0.)')
    parser.add_argument('-p', '--print', action='store_true',
                        help='split ascii image into files for print')
    parser.add_argument('--page-width', type=int, default=75,
                        help='page width (char); use with --print')
    parser.add_argument('--page-height', type=int, default=150,
                        help='page height (char); use with --print')
    parser.add_argument('-v', '--version', action='version',
                        version=asciimg.__version__,
                        help='show the version number and exit')

    args = parser.parse_args()

    return args


def main():
    args = get_args()
    contrast = max(0., args.contrast)

    try:
        img_ascii = img_to_ascii(args.image, args.width, contrast)
    except FileNotFoundError as e:
        print('Error: {}'.format(e), file=sys.stderr)
        sys.exit(-1)

    if args.print:
        img_print(img_ascii, args.image, args.page_width, args.page_height)
    else:
        print(img_ascii)


if __name__ == '__main__':
    main()

