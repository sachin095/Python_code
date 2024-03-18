# a = {9, 6, 7, 7, 6, 9,}
# b = {55, 88, 7, 0,  5}
# #print(a.pop())
# print(a.union(b))
# print(b.intersection(a))
# #print(a.copy(b))
# print(a)
# print(b)
import turtle
import random

# Screen setup
turtle.bgcolor("black")
turtle.speed(0)
turtle.title("Irregular Matrix Pattern with Floating Lines")
turtle.colormode(255)  # Allows to use RGB color values

# Function to draw a single line
def draw_line(x, y, length, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.forward(length)

# Function to draw a random dot
def draw_dot(x, y, size, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.dot(size, color)

# Function to generate random colors
def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

# Main drawing function
def draw_pattern():
    for _ in range(100):  # Number of elements in the pattern
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        length = random.randint(20, 100)  # Line length
        size = random.randint(5, 20)  # Dot size
        color = random_color()

        # Randomly choose to draw either a line or a dot
        if random.choice([True, False]):
            draw_line(x, y, length, color)
        else:
            draw_dot(x, y, size, color)

        # Optional: draw floating lines
        if random.choice([True, False]):
            # Draw a line that extends outside the initial line or dot
            draw_line(x+length, y, length//2, color)  # Floating effect

if __name__ == "__main__":
    draw_pattern()
    turtle.hideturtle()
    turtle.done()
