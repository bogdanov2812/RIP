from Classes.rectangle import Rectangle
from Classes.circle import Circle
from Classes.square import Square


def main():
    r = Rectangle("желтого", 8, 9)
    c = Circle("оранжевого", 4)
    s = Square("красного", 7)
    print(r)
    print(c)
    print(s)

if __name__ == "__main__":
    main()