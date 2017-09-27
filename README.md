# asciimg - convert image into ASCII text

This is a simple console app used to convert images into ASCII text. The resulting ascii text could be split into pages for printing.

## Usage

It's dead simple :)
```
$ ./asciimg.py kitty.png
```
Also, you can specify a width of the resulting ascii text in chars using `-w` argument. A contrast of the image could be adjusted with the `-c` argument. You can also split the resulting ascii text into multiple `.txt` files for printing by providing a `-p` argument and specifying width and height parameters of the page. Run `$ ./asciimg.py --help` to see all arguments.

## Example:

![](./kitty.png)

## Dependencies

In order to run this app make sure the following packages are installed:

* [Pillow](https://python-pillow.org/)
* [NumPy](http://www.numpy.org)

Use `pip` to install them:
```
$ pip3 install --user pillow numpy
```

## License

This software is distributed under the terms of the [MIT](https://opensource.org/licenses/MIT) license.

