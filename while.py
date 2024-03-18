#i = 0
#while(i<10):
 #   print(i)
  #  i +=1
    
#while(True):
 #   num = int(input("enter number: "))
# for i in range(10):
#     if (i == 10):
#         break
#     print(0+i)
# else:
#     print("finish")
# a = "hello world.I am python."
# for i in a:
#     if i != ".":
#         print(i)
import turtle
import random

# Set up the screen
turtle.bgcolor("black")
turtle.speed(0)  # Set the drawing speed to the fastest
turtle.title("Complex Pattern Example")

# Create a function to draw a circle using turtle with dynamic size and color
def draw_circle(radius, color):
    turtle.color(color)
    turtle.circle(radius)
    turtle.right(60)

# Function to draw multiple circles to form a complex pattern
def draw_pattern():
    for _ in range(12):  # Repeat 12 times to form a circular pattern
        draw_circle(100, "red")
        draw_circle(80, "blue")
        draw_circle(60, "green")
        draw_circle(40, "yellow")
        draw_circle(20, "purple")
        turtle.right(30)  # Adjust the angle for the pattern

# Main function to execute the drawing
def main():
    turtle.penup()  # Pull the pen up – no drawing when moving.
    turtle.goto(0, -100)  # Move turtle to an initial position
    turtle.pendown()  # Pull the pen down – drawing when moving.
    draw_pattern()
    turtle.hideturtle()  # Hide the turtle after drawing is complete
    turtle.done()  # Keep the window open until it is closed by the user

if __name__ == "__main__":
    main()

    
    
    