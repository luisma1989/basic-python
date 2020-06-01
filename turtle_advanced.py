import turtle


def main():
    turtle.Screen()
    box = turtle.Turtle()

    make_square(box)

    turtle.mainloop()


def make_square(box):
    length = int(input('Tamaño: '))
    for i in range(4):
        make_line_and_turn(box, length)


def make_line_and_turn(box, length):
    box.forward(length)
    box.left(90)


if __name__ == "__main__":
    main()
