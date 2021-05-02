import tkinter as tk
import datetime as dt
from tkinter import simpledialog, messagebox, Tk, Canvas, HIDDEN, NORMAL, Button, ARC, CHORD
import sys
r"""
First_screen = tk.Tk()
First_screen.title("Hi, world")
First_screen.wm_iconbitmap("Pattern.png")
fst_part_of_screen = tk.Canvas(First_screen, width=1024, height=720, bg="cyan")
fst_part_of_screen.pack()
fst_part_of_screen.create_text(0, 0, fill="dark red", text="Hi,world", anchor="nw", font="Arial 90 ")
   First_screen.mainloop()



def return_good_days_left(d1 , d2):
    return str(d2-d1).split(" ")[0]
def make_formatted_date():
    list_of_events = []
    for line in open("Hello.txt"):
        my_current_event = line.strip()
        my_current_event = my_current_event.split(", ")
        my_current_event[1] = dt.datetime.strptime(my_current_event[1], "%Y-%m-%d").date()
        list_of_events.append(my_current_event)
    return list_of_events


second_screen = tk.Tk()
second_screen.title("......................Binod's devil  House...............")
first_part_of_screen = tk.Canvas(second_screen, width=1030, height=760, bg="red")
first_part_of_screen.pack()
first_part_of_screen.create_text(515, 0, font="Arial 24 underline italic", anchor="n",
                                 text="Hi, world, I have some dates, you might wanna follow.")

returned_list = make_formatted_date()
today = dt.date.today()
#write_it_down(returned_list, today)

y_pixels = 40
returned_list.sort(key=lambda x: x[1])
for data in returned_list:
    d2 = data[1]
    first_part_of_screen.create_text(515+y_pixels, y_pixels, font="Arial 18 bold", anchor="n",
                     text=("It's %s days left for %s" %(return_good_days_left(today, d2), data[0])))
    y_pixels += 40
tk.mainloop()
# Hello.txt
#Dashain, 2020-10-15
#Tihar, 2020-11-15
#Maghe Sankrati, 2021-01-16
#Maha Shivaratri, 2021-02-05
#Holi, 2021-03-25

create = tk.Tk()
create.withdraw()
my_country_city_dict = {}
def city_country():
    for city_country in open("Hello.txt"):
        city_country.strip()
        city_country = list(city_country.partition("/"))
        city_country.pop(1)
        my_country_city_dict[city_country[0]] = city_country[1]
    return my_country_city_dict
def add_data(country, data):
    with open("Hello.txt", "a") as file:
        file.write("\n" + country + "/" + data)
    my_country_city_dict[country] = [data]

while True:
    a = (simpledialog.askstring("Questions coming around", "I'll tell capital of any country you enter here: ")).title()
    c = city_country()
    if a in c.keys():
        messagebox.showinfo("Answer: ", c[a])
    else:
        k = (simpledialog.askstring("Learning now:", "Please teach me the capital of " + a)).title()
        add_data(a, k)
        messagebox.showinfo("Thanks I'll remember it." + k)


import random

screen = tk.Tk()
screen.withdraw()


def cipher(message_to_encrypt_or_decrypt):
    even_message_list = []
    odd_message_list = []
    message_list = []
    message_to_encrypt_or_decrypt_list = list(message_to_encrypt_or_decrypt)
    if len(message_to_encrypt_or_decrypt_list) % 2 != 0:
        message_to_encrypt_or_decrypt_list += "h"
        message_to_encrypt_or_decrypt += "h"
    for i in range(0, len(message_to_encrypt_or_decrypt_list), 2):
       even_message_list.append(message_to_encrypt_or_decrypt_list[i])
    for j in range(1, len(message_to_encrypt_or_decrypt_list), 2):
        odd_message_list.append(message_to_encrypt_or_decrypt_list[j])
    for k in range(int(len(message_to_encrypt_or_decrypt_list)/2)):
        message_list.append(even_message_list[k])
        message_list.append(odd_message_list[k])

    return "".join(message_list)


def extreme_encrypter(message_to_encrypt):
    message_to_encrypt_list = cipher(message_to_encrypt)
    reversed_message = "".join(reversed(message_to_encrypt_list))
    encrypted_message_list = []
    for i in range(len(reversed_message)):
        encrypted_message_list.append(random.choice("abcdefghijklmnopqrstuvwxyz"))
        encrypted_message_list.append(reversed_message[i])
    return "".join(encrypted_message_list)


def extreme_decrypter(message_to_decrypt):
    message_to_decrypt_list = list(message_to_decrypt)
    message_to_decrypt_list_temp = []
    for i in range(1, len(message_to_decrypt), 2):
        message_to_decrypt_list_temp.append(message_to_decrypt_list[i])

    partially_decrypted_message = "".join(reversed(message_to_decrypt_list_temp))
    decrypted_message = cipher(partially_decrypted_message)

    return decrypted_message


#### I wrote this decryptor before I realized I could use cipher only:
# def decrypt(message_to_decrypt):
# message_to_decrypt_list = list(message_to_decrypt)
# if len(message_to_decrypt) % 2 == 0:
#  for i in range(0, len(message_to_decrypt), 2):
#       message_to_decrypt_list[i + 1] = message_to_decrypt[i]
#        message_to_decrypt_list[i] = message_to_decrypt[i + 1]
# else:
#      for i in range(0, len(message_to_decrypt) - 1, 2):
#      message_to_decrypt_list[i] = message_to_decrypt[i + 1]
#           message_to_decrypt_list[i + 1] = message_to_decrypt[i]
#    return "".join(message_to_decrypt_list)

while True:
    choice = simpledialog.askstring("It's all your choice", "Do you wanna continue? (Yes/No/Y/S): ", )
    if choice.lower() == "yes" or choice.lower() == "y":
        encrypt_or_decrypt = simpledialog.askstring("Choose whether", "Do you want Encryption or decryption?: (E/D)")
        if encrypt_or_decrypt.lower() == "e":
            message_to_encrypt = simpledialog.askstring("...Give me your code...I'm ready for encryption ",
                                                        "Just tell me what you wanna encrypt: ")
            message = extreme_encrypter(message_to_encrypt)
            messagebox.showinfo("See what I cooked for you: ", message)

        elif encrypt_or_decrypt.lower() == "d":
            message_to_decrypt = simpledialog.askstring("...Give me your code...I'm ready for decryption ",
                                                        "Just tell me what you wanna decrypt: ")
            message = extreme_decrypter(message_to_decrypt)
            messagebox.showinfo("See what I cooked for you: ", message)
        else:
            raise ValueError("Used %s instead of E or D" % encrypt_or_decrypt)

    elif choice.lower() == "no" or choice.lower() == "n":
        break
    else:
        raise ValueError("Used %s instead of Yes or No or Y or N" % choice)

from tkinter import HIDDEN, NORMAL, Tk, Canvas
def toggle_eyes():
    current_color = c.itemcget(eye_left, 'fill')
    new_color = c.body_color if current_color == 'white' else 'white'
    current_state = c.itemcget(pupil_left, 'state')
    new_state = NORMAL if current_state == HIDDEN else HIDDEN
    c.itemconfigure(pupil_left, state=new_state)
    c.itemconfigure(pupil_right, state=new_state)
    c.itemconfigure(eye_left, fill=new_color)
    c.itemconfigure(eye_right, fill=new_color)
root = Tk()
c = Canvas(root, width=700, height=700)
c.configure(bg='dark blue', highlightthickness=0, )
c.body_color = 'Black'
body = c.create_oval(35, 20, 365, 350, outline=c.body_color, fill=c.body_color)
ear_left = c.create_polygon(75, 80, 75, 10, 165, 70, outline=c.body_color, fill="red")
ear_right = c.create_polygon(255, 45, 325, 10, 320, 70, outline=c.body_color, fill="red")
foot_left = c.create_oval(65, 320, 145, 360, outline=c.body_color, fill=c.body_color)
foot_right = c.create_oval(250, 320, 330, 360, outline=c.body_color, fill=c.body_color)
eye_left = c.create_oval(130, 110, 160, 170, outline='black', fill='white')
pupil_left = c.create_oval(140, 145, 150, 155, outline='black', fill='black')
eye_right = c.create_oval(230, 110, 260, 170, outline='black', fill='white')
pupil_right = c.create_oval(240, 145, 250, 155, outline='black', fill='black')
mouth_normal = c.create_line(100, 250, 200, 272, 300, 250, fill="white", smooth=1, width=2, state=NORMAL)
c.itemcget()
c.pack()
root.mainloop()


import random
import time


def next_shape():
    print(shapes)
    global shape
    global previous_color
    global current_color
    previous_color = current_color
    c.delete(shape)
    if len(shapes) > 0:
        shape = shapes.pop()
        c.itemconfigure(shape, state=NORMAL)
        current_color = c.itemcget(shape, 'fill')
        root.after(1000, next_shape)
    else:
        c.unbind('q')
        c.unbind('p')
        if player1_score > player2_score:
            c.create_text(200, 200, text='Winner: Player 1')
        elif player2_score > player1_score:
            c.create_text(200, 200, text='Winner: Player 2')
        else:
            c.create_text(200, 200, text='Draw')
        c.pack()


def snap(event):
    global shape
    global player1_score
    global player2_score
    valid = False
    c.delete(shape)
    if previous_color == current_color:
        valid = True
    if valid:
        if event.char == 'q':
            player1_score = player1_score + 1
        else:
            player2_score = player2_score + 1
        text = c.create_text(200, 200, text='SNAP! You score 1 point!')
    else:
        if event.char == 'q':
            player1_score = player1_score - 1
        else:
            player2_score = player2_score - 1
        text = c.create_text(200, 200, text='WRONG! You lose 1 point!')
    c.pack()
    root.update_idletasks()
    time.sleep(1)
    c.delete(text)


colors = ("black", "red", "green", "blue", "yellow", "orange", "pink", "grey", "purple", "cyan")

root = Tk()
root.title('Snap')
c = Canvas(root, width=400, height=400, )
shapes = []
for color in colors:
    circle = c.create_oval(35, 20, 365, 350, outline=color, fill=color, state=HIDDEN)
    shapes.append(circle)

for color in colors:
    rectangle = c.create_rectangle(35, 100, 365, 270, outline=color, fill=color, state=HIDDEN)
    shapes.append(rectangle)

for color in colors:
    square = c.create_rectangle(35, 20, 365, 350, outline=color, fill=color, state=HIDDEN)
    shapes.append(square)

c.pack()
random.shuffle(shapes)
shape = None
previous_color = ''
current_color = ''
player1_score = 0
player2_score = 0
root.after(3000, next_shape)
c.bind('q', snap)
c.bind('p', snap)
c.focus_set()
tk.mainloop()

import random
import time
from tkinter import Tk, Button, DISABLED

def show_symbol(x, y):

    global first
    global previousX, previousY
    buttons[x, y]['text'] = button_symbols[x, y]
    buttons[x, y].update_idletasks()
    if first:
        previousX = x
        previousY = y
        first = False
    elif previousX != x or previousY != y:
        if buttons[previousX, previousY]['text'] != buttons[x, y]['text']:
            time.sleep(0.5)
            buttons[previousX, previousY]['text'] = ''
            buttons[(x, y)]['text'] = ''
        else:
            buttons[previousX, previousY]['command'] = DISABLED
            buttons[x, y]['command'] = DISABLED
        first = True



root = Tk()
root.title('Matchmaker')
root.geometry("1024x730")
buttons = {}
first = True
previousX = 0
previousY = 0
button_symbols = {}
symbols = [u'\u2702', u'\u2702', u'\u2705', u'\u2705', u'\u2708', u'\u2708',
           u'\u2709', u'\u2709', u'\u270A', u'\u270A', u'\u270B', u'\u270B',
           u'\u270C', u'\u270C', u'\u270F', u'\u270F', u'\u2712', u'\u2712',
           u'\u2714', u'\u2714', u'\u2716', u'\u2716', u'\u2728', u'\u2728']

random.shuffle(symbols)
for x in range(4):
    for y in range(6):
        button = Button(command=lambda x=x, y=y: show_symbol(x, y), text=" I am?", width=10, height=4, anchor="n", )
        button.grid(column=x, row=y)
        buttons[x, y] = button
        button_symbols[x, y] = symbols.pop()
root.mainloop()

import time
import itertools
import random

colors = ["white", "blue", "pink", "black", "red", "green", "grey"]
random.shuffle(colors)
iter_colors = itertools.cycle(colors)


class MyGame:
    pass
def replay_game():
    MyGame.root.minsize(width=800, height=600)
    MyGame.no_of_eggs = 0
    MyGame.canvas = Canvas(MyGame.root, width=1024, height=730, bg="deep sky blue")
    MyGame.canvas.create_oval(-100, 100, 100, -100, fill="yellow")
    MyGame.canvas.create_rectangle(0, 550, 1024, 730, fill="green")
    MyGame.life = 5
    MyGame.score = 0
    MyGame.basket = MyGame.canvas.create_arc(100, 500, 300, 700, start=180, extent=180, style=ARC, width=30)
    MyGame.canvas.bind("<Left>", move_left)
    MyGame.canvas.bind("<Right>", move_right)
    MyGame.canvas.focus_set()
    MyGame.eggs = []
    MyGame.speed = 50
    MyGame.display_score = MyGame.canvas.create_text(10, 20, anchor="nw", text="Score< " + str(MyGame.score) + " >",
                                                     fill="Green",
                                                     font="Arial 20")

    MyGame.display_life = MyGame.canvas.create_text(900, 20, anchor="e", text="\u2764" * MyGame.life, fill="Dark red",
                                                    font="Arial 20")
    MyGame.display_speed_pixel = MyGame.canvas.create_text(500, 20, anchor="n",
                                                           text="Speed: " + str(MyGame.speed) + "pp/500ms",
                                                           font="Arial 20")
    MyGame.root.update_idletasks()

    begin_game()
    MyGame.root.mainloop()
def start_rendering():
    a.destroy()
    begin_game()
def begin_game():

    create_eggs()
    move_eggs()
    check_catch()
    update_score_lives_and_speed()


def create_eggs():
    new_color = next(iter_colors)
    MyGame.egg = MyGame.canvas.create_oval(n := random.randint(100, 800), 10, n + 50, 100, fill=new_color)
    MyGame.eggs.append(MyGame.egg)
    MyGame.canvas.pack()
    if MyGame.life != 0:
        MyGame.root.after(3000, create_eggs)


def move_eggs():
    loc_speed = speed()
    for egg in MyGame.eggs:
        egg_x, egg_y, egg_x2, egg_y2 = MyGame.canvas.coords(egg)
        MyGame.canvas.move(egg, 0, loc_speed)
    MyGame.root.after(500, move_eggs)


def check_catch():
    (basket_x1, basket_y1, basket_x2, basket_y2) = MyGame.canvas.coords(MyGame.basket)
    update_score_lives_and_speed()
    for egg in MyGame.eggs:
        (egg_x, egg_y, egg_x2, egg_y2) = MyGame.canvas.coords(egg)
        if (basket_x1 < egg_x) and (egg_x2 < basket_x2) and (basket_y2 - egg_y2) < 40:
            score_adder(egg)
            MyGame.eggs.remove(egg)
            MyGame.canvas.delete(egg)
            MyGame.no_of_eggs -= 1
        elif egg_y2 >= 700 and (col:=MyGame.canvas.itemcget(egg, "fill")!="red"):
            egg_deletor(egg)
    MyGame.root.after(100, check_catch)


def update_score_lives_and_speed():
    MyGame.canvas.itemconfigure(MyGame.display_life, text="\u2764" * MyGame.life, fill="Dark red")
    MyGame.canvas.itemconfig(MyGame.display_score, text="Score< " + str(MyGame.score) + " >")
    MyGame.canvas.itemconfig(MyGame.display_speed_pixel, text="Speed: " + str(round(MyGame.speed, 4)) + "pp/500ms")
    MyGame.canvas.pack()


def egg_deletor(egg):
    MyGame.eggs.remove(egg)
    MyGame.canvas.delete(egg)
    MyGame.no_of_eggs -= 1
    MyGame.life -= 1

    if MyGame.life == 0:
        lost()


def score_adder(egg):
    if (color:=MyGame.canvas.itemcget(egg, "fill"))=="black":
        MyGame.score += 30
    elif (color:=MyGame.canvas.itemcget(egg, "fill"))=="red":
        MyGame.score -= 10
    else:
        MyGame.score += 10

def lost():
    a = messagebox.askyesno(title="Lost", message="You've lost", detail="Wanna play again?")
    if a==True:
        ender()
        MyGame.root=Tk()
        MyGame.canvas = Canvas(MyGame.root, width=1024, height=730, bg="deep sky blue")
     

        replay_game()
    else:
        ender()


def ender():
    MyGame.root.destroy()

def speed():
    MyGame.speed += 0.01
    return MyGame.speed


def move_left(event):
    (x1, y1, x2, y2) = MyGame.canvas.coords(MyGame.basket)
    if x1 > 0:
        MyGame.canvas.move(MyGame.basket, -20, 0)


def move_right(event):
    (x1, y1, x2, y2) = MyGame.canvas.coords(MyGame.basket)
    if x2 < 1024:
        MyGame.canvas.move(MyGame.basket, 20, 0)


MyGame.root = Tk()
MyGame.root.minsize(width=800, height=600)
a = Button(MyGame.root, command=start_rendering, text="Do you wanna play my eggs?, just hit me hard", fg="blue", padx=100, pady=100)
a.pack(padx=100, pady=100)
MyGame.no_of_eggs = 0
MyGame.canvas = Canvas(MyGame.root, width=1024, height=730, bg="deep sky blue")
MyGame.canvas.create_oval(-100, 100, 100, -100, fill="yellow")
MyGame.canvas.create_rectangle(0, 550, 1024, 730, fill="green")
MyGame.life = 5
MyGame.score = 0
MyGame.basket = MyGame.canvas.create_arc(100, 500, 300, 700, start=180, extent=180, style=ARC, width=30)
MyGame.canvas.bind("<Left>", move_left)
MyGame.canvas.bind("<Right>", move_right)
MyGame.canvas.focus_set()
MyGame.eggs = []
MyGame.speed = 50
MyGame.display_score = MyGame.canvas.create_text(10, 20, anchor="nw", text="Score< " + str(MyGame.score) + " >",
                                                 fill="Green",
                                                 font="Arial 20")

MyGame.display_life = MyGame.canvas.create_text(900, 20, anchor="e", text="\u2764" * MyGame.life, fill="Dark red",
                                                font="Arial 20")
MyGame.display_speed_pixel = MyGame.canvas.create_text(500, 20, anchor="n",
                                                       text="Speed: " + str(MyGame.speed) + "pp/500ms",
                                                       font="Arial 20")
MyGame.root.mainloop()
"""

