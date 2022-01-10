import turtle

def main():
    # Create a turtle object
    michaelangelo = turtle.Turtle()
    michaelangelo.speed(12)
    michaelangelo.color("blue")

    # Ask the turtle to move around the canvas
    for i in range(1000):
        michaelangelo.forward(15 + i)
        michaelangelo.right(225)


    turtle.exitonclick()

if __name__ == "__main__":
    main()

