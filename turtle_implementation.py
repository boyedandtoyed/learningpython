import turtle as t

t.Screen().title("Binod's......................................................................Freaky world")
"""
t.shape("turtle")
t.penup()
t.speed("slow")
def make_rectangle(horizontal, verticle, color):
    t.pendown()
    t.color(color)
    t.begin_fill()
    for i in range(2):
        t.forward(horizontal)
        t.left(90)
        t.fd(verticle)
        t.left(90)
    t.end_fill()
    t.penup()

#face
t.goto(-50, 150)
make_rectangle(100, 100, "pink")
#mouth
t.goto(-10, 160)
make_rectangle(20, 20, "red")
#eyes
t.goto(-50, 230)              # -45, and 200
make_rectangle(30, 20,"black")
t.goto(20, 150)              # 10 and 200
make_rectangle(30, 20,"black")
#neck
t.goto(-25, 100)
make_rectangle(50, 50,"pink")
#hands
t.goto(-100, 0)
make_rectangle(30, 100,"Blue")
t.goto(70, 0)
make_rectangle(30, 100,"blue")
t.goto(-70, 70)
make_rectangle(20, 30,"blue")
t.goto(50, 70)
make_rectangle(20, 30,"blue")
#Body
t.goto(-50, 0)
make_rectangle(100, 100,"Orange")
#legs
t.goto(-50, -200)
make_rectangle(15, 200, "yellow")
t.goto(35, -200)
make_rectangle(15, 200, "yellow")
#toes
t.goto(-100, -250)
make_rectangle(65, 50, "Green")
t.goto(35, -250)
make_rectangle(65, 50, "green")
t.hideturtle()

t.bgpic(r"C:/Users/Hp/Downloads/SHAREit/SM-J710F/photo/20200408_203241.jpg")
integer=0
t.speed("fast")
t.hideturtle()
t.pencolor("red")
while True:
    t.setheading(integer)
    for i in range(2):
        t.forward(100)
        t.left(90)
        t.forward(100)
        t.left(90)
    integer += 5

import itertools as it
mr_color = it.chain(["red", "black", "orange", "green", "blue", "yellow", "pink", ""]*100)
t.right(100)
def draw_circles(size,forward):
    t.bgcolor(next(mr_color))
    t.color(next(mr_color))
    t.begin_fill()
    t.left(90)
    t.circle(size)
    t.right(45)
    t.circle(size)
    t.end_fill()
    draw_circles(size+1, 1)
t.speed("fastest")
draw_circles(10, 20)

import itertools as it
import random

bglist = ["gold", "silver", "maroon"] * 100
mr_color = it.chain(["red", "black", "orange", "green", "blue", "yellow", "pink", ""] * 100)
t.hideturtle()
def draw_shapes(cir_diam=0, sq_len=0, shape=None, integer=0):
    local_color = next(mr_color)
    bgcolor = bglist[random.choice([0, 1, 2, 3])]
    t.bgcolor(bgcolor)
    print(integer)
    t.setheading(integer)
    if shape.lower() == "circle":
        t.color(local_color)
        t.begin_fill()
        t.circle(cir_diam)
        t.end_fill()
        integer += 1
        draw_shapes(cir_diam, sq_len, shape, integer)
    if shape.lower() == "square":
        t.color(local_color)
        t.begin_fill()
        t.setheading(integer)
        for i in range(2):
            t.forward(sq_len)
            t.left(90)
            t.forward(sq_len)
            t.left(90)
        t.end_fill()
        integer += 1
        draw_shapes(cir_diam, sq_len, shape, integer)
t.speed("fastest")
draw_shapes(sq_len=100, shape="squaRe")

t.Screen().bgcolor("yellow")

import random

list = [x for x in range(5, 10) if x != 0]
list_of_colors = ["orange", "white", "red", "yellow"]
list_of_row_or_vertical = [x for x in range(-350, 350, 1)]
list_of_column_or_horizontal = [x for x in range(-500, 501, 1)]
def random_generator(x, y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(random.random(), random.random(), random.random())
    t.begin_fill()

def stars(points, ):
    t.penup()
    t.onscreenclick(fun=random_generator)
    t.pendown()
    random_length = random.randint(10, 20)
    for i in range(points):
        angle = 180 - (180 / points)
        t.forward(random_length)
        t.right(angle)
    t.end_fill()
    points = random.choice(list)
    stars(points)
x = random.choice(list)
t.speed("fastest")
stars(x)

import random
t.colormode(255)
t.shape("turtle")
t.speed("fastest")
cols = ["white", "green", "pink", "Black"]
def return_coordinate(x, y):
    if x == 0 and y == 0:
        goto_coord = [random.randint(-int((t.window_width()) / 2), int((t.window_width()) / 2)),
                      random.randint(-int((t.window_height()) / 2), int((t.window_height()) / 2))]
        t.penup()
        t.goto(goto_coord[0], goto_coord[1])
        t.pendown()
    else:
        goto_coord = [x, y]
        t.penup()
        t.goto(goto_coord[0], goto_coord[1])
        t.pendown()


def inside_window():
    width_info_left = (-((t.window_width()) / 2)) + 500
    height_info_down = (-((t.window_height()) / 2)) + 500
    width_info_right = (((t.window_width()) / 2)) - 500
    height_info_up = (((t.window_height()) / 2)) - 500
    x, y = t.pos()
    boolean = (width_info_left < x < width_info_right) and (height_info_down < y < height_info_up)
    return boolean
def random_lines1(cols=cols):
    random_lines(cols)

def random_lines(cols):
    rand_cols = random.choice(cols)
    forward = random.randint(10, 200)
    t.bgcolor("black")
    t.right(random.randint(1, 180))
    t.color(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
    t.pensize(random.randint(10, 30))
    t.onscreenclick(fun=return_coordinate)



    if inside_window():
        t.forward(forward)
        t.fillcolor(rand_cols)
        t.shapesize()
        t.stamp()
        random_lines1()

    else:
        t.penup()
        t.goto(random.randint(-300, 300), random.randint(-300, 300))
        t.pendown()
        t.forward(forward)
        random_lines1()

random_lines((cols))

import random
def outside_window():
    left_wall = -t.window_width() / 2
    right_wall = t.window_width() / 2
    top_wall = t.window_height() / 2
    bottom_wall = -t.window_height() / 2
    (x, y) = caterpillar.pos()
    outside = x < left_wall or x > right_wall or y < bottom_wall or y > top_wall
    return outside


def start_game():
    global game_started
    if game_started:
        return
    game_started = True
    score = 0
    text_turtle.clear()
    caterpillar_speed = 2
    caterpillar_length = 3
    caterpillar.shapesize(1, caterpillar_length, 1)
    caterpillar.showturtle()
    display_score(score)
    place_leaf()
    while True:
        caterpillar.forward(caterpillar_speed)
        if caterpillar.distance(leaf) < 20:
            place_leaf()
            caterpillar_length = caterpillar_length + 1
            caterpillar.shapesize(1, caterpillar_length, 1)
            caterpillar_speed = caterpillar_speed + 1
            score = score + 10
            display_score(score)
        if outside_window():
            game_over()
            break
def game_over():
    caterpillar.color('yellow')
    leaf.color('yellow')
    t.penup()
    t.hideturtle()
    t.write('GAME OVER!', align='center', font=('Arial', 30, 'normal'))


def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width() / 2) - 50
    y = (t.window_height() / 2) - 50
    score_turtle.setpos(x, y)
    score_turtle.write(str(current_score), align='right', font=('Arial', 40, 'bold'))

def place_leaf():
    leaf.ht()

    leaf.setx(random.randint(-200, 200))
    leaf.sety(random.randint(-200, 200))
    leaf.st()
def move_up():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(90)
def move_down():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(270)
def move_left():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(180)
def move_right():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(0)

t.bgcolor("grey")
caterpillar = t.Turtle()
caterpillar.shape('square')
caterpillar.color('red')
caterpillar.speed(0)
caterpillar.penup()
caterpillar.hideturtle()
leaf = t.Turtle()
leaf.color("green")
leaf_shape = ((0, 0), (14, 2), (18, 6), (20, 20), (6, 18), (2, 14))
t.register_shape("leaf", leaf_shape)
leaf.shape("leaf")
leaf.penup()
leaf.hideturtle()
leaf.speed(0)
game_started = False
text_turtle = t.Turtle()
text_turtle.hideturtle()
text_turtle.write('Freaking start', align='center', font=('Arial', 16, 'bold'))
score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

t.onkey(start_game, 'space')
t.onkey(move_up, 'Up')
t.onkey(move_right, 'Right')
t.onkey(move_down, 'Down')
t.onkey(move_left, 'Left')
t.listen()
t.mainloop()


from Timely import prime_numbers as pm
a = pm(1000)
t.hideturtle()
k = 1
t.penup()
t.goto(-450,0)
t.pendown()

for i in a:
	t.circle(i)
	t.penup()
	t.forward(a[k])

	t.pendown()
	k += 1 if k < len(a) else 0
"""







