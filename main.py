from items.item import *


def main():
    saber = item("Light Saber", "A laser sword", 70)
    contents = []
    contents += saber
    box = container("Box", "a small metal box", 5, contents)
    print(box.__str__)
