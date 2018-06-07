# asciimg - convert image into ASCII text

This is a simple console app which is used to convert images into ASCII text. The resulting ascii text could be split into pages for printing.

## Usage

Just provide a path to a target image:
```
./asciimg.py kitty.png
```
Also, you can specify a width of the resulting ascii text in chars using `-w` argument. A contrast of the image could be adjusted with the `-c` argument. You can also split the resulting ascii text into multiple `txt` files for printing by providing a `-p` argument and specifying width and height parameters of the page.

## Output

![](../assets/kitty.png?raw=true)

## Install

In order to run this app make sure the following frameworks are installed:

* [Pillow](https://python-pillow.org/)
* [NumPy](http://www.numpy.org)

You can use `pip` to install them:
```
$ pip3 install --user -r requirements.txt
```

