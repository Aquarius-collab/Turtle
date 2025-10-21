import turtle
turtle.Screen().bgcolor("Blue")
sc = turtle.Screen()
sc.setup(600,500)
turtle.title("Welcome to Turtle")
board = turtle.Turtle()
for i in range(4):
    board.forward(100)
    board.left(90)
    i = i+1
