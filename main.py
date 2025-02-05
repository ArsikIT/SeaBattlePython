from tkinter import *
from tkinter import messagebox
import time
import random

tk = Tk()
app_running = True

size_canvas_x = 500
size_canvas_y = 500
s_x = s_y = 8  # size of the game field - not less than 8 and not more than 18
#s_y = 8
step_x = size_canvas_x // s_x  # step in the horizontal direction
step_y = size_canvas_y // s_y  # step in the vertical direction
size_canvas_x = step_x * s_x
size_canvas_y = step_y * s_y

txt_len_middle = "* Human vs Computer"
size_font_x = 10
len_txt_x = len(txt_len_middle) * size_font_x
print(len_txt_x)
delta_menu_x = len_txt_x // step_x + 1
menu_x = step_x * delta_menu_x  # 250

menu_y = 40
ships = s_x // 2  # maximum number of ships
ship_len1 = s_x // 5  # length of the first type of ship
ship_len2 = s_x // 3  # length of the second type of ship
ship_len3 = s_x // 2  # length of the third type of ship
enemy_ships1 = [[0 for i in range(s_x + 1)] for i in range(s_y + 1)]
enemy_ships2 = [[0 for i in range(s_x + 1)] for i in range(s_y + 1)]
list_ids = []  # list of canvas objects

# points1 - list of where we clicked with the mouse
points1 = [[-1 for i in range(s_x)] for i in range(s_y)]
points2 = [[-1 for i in range(s_x)] for i in range(s_y)]

# boom - list of hits on enemy ships
boom = [[0 for i in range(s_x)] for i in range(s_y)]

# ships_list - list of ships for player 1 and player 2
ships_list = []

# player_turn_1 - if True, it's Player 2's turn, otherwise it's Player 1's turn
player_turn_1 = False

# computer_vs_human - if True, the game is played against the computer
computer_vs_human = False
if computer_vs_human:
    add_to_label = " (Computer)"
    add_to_label2 = " (targeting)"
    player_turn_1 = False
else:
    add_to_label = ""
    add_to_label2 = ""
    player_turn_1 = False

# Function to close the game window safely
def on_closing():
    global app_running
    if messagebox.askokcancel("Exit Game", "Do you want to exit the game?"):
        app_running = False
        tk.destroy()

tk.protocol("WM_DELETE_WINDOW", on_closing)
tk.title("Battleship Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=size_canvas_x + menu_x + size_canvas_x, height=size_canvas_y + menu_y, bd=0,
                highlightthickness=0)
canvas.create_rectangle(0, 0, size_canvas_x, size_canvas_y, fill="white")
canvas.create_rectangle(size_canvas_x + menu_x, 0, size_canvas_x + menu_x + size_canvas_x, size_canvas_y,
                        fill="lightyellow")
canvas.pack()
tk.update()

# Function to draw the game field grid
def draw_table(offset_x=0):
    for i in range(0, s_x + 1):
        canvas.create_line(offset_x + step_x * i, 0, offset_x + step_x * i, size_canvas_y)
    for i in range(0, s_y + 1):
        canvas.create_line(offset_x, step_y * i, offset_x + size_canvas_x, step_y * i)

draw_table()
draw_table(size_canvas_x + menu_x)

# Labels for Player 1 and Player 2
t0 = Label(tk, text="Player №1", font=("Helvetica", 16))
t0.place(x=size_canvas_x // 2 - t0.winfo_reqwidth() // 2, y=size_canvas_y + 3)
t1 = Label(tk, text="Player №2" + add_to_label, font=("Helvetica", 16))
t1.place(x=size_canvas_x + menu_x + size_canvas_x // 2 - t1.winfo_reqwidth() // 2, y=size_canvas_y + 3)

t0.configure(bg="red")
t0.configure(bg="#f0f0f0")

t3 = Label(tk, text="@@@@@@@", font=("Helvetica", 16))
t3.place(x=size_canvas_x + menu_x//2 - t3.winfo_reqwidth() // 2, y= size_canvas_y)

# Function to switch game modes (Human vs Computer or Human vs Human)
def change_rb():
    global computer_vs_human, add_to_label, add_to_label2
    print(rb_var.get())
    if rb_var.get():
        computer_vs_human = True
        add_to_label = " (Computer)"
        add_to_label2 = " (targeting)"
    else:
        computer_vs_human = False
        add_to_label = ""
        add_to_label2 = ""

rb_var = BooleanVar()
rb1 = Radiobutton(tk, text="Human vs Computer", variable=rb_var, value=1, command=change_rb)
rb2 = Radiobutton(tk, text="Human vs Human", variable=rb_var, value=0, command=change_rb)
rb1.place(x=size_canvas_x + menu_x // 2 - rb1.winfo_reqwidth() // 2, y=140)
rb2.place(x=size_canvas_x + menu_x // 2 - rb2.winfo_reqwidth() // 2, y=160)
if computer_vs_human:
    rb1.select()

# Function to mark the current player's turn
def mark_player(player_mark_1):
    if player_mark_1:
        t0.configure(bg="red")
        t0.configure(text="Player №1" + add_to_label2)
        t0.place(x=size_canvas_x // 2 - t0.winfo_reqwidth() // 2, y=size_canvas_y + 3)
        t1.configure(text="Player №2" + add_to_label)
        t1.place(x=size_canvas_x + menu_x + size_canvas_x // 2 - t1.winfo_reqwidth() // 2, y=size_canvas_y + 3)
        t1.configure(bg="#f0f0f0")
        t3.configure(text="Player №2's Turn" + add_to_label)
        t3.place(x=size_canvas_x + menu_x // 2 - t3.winfo_reqwidth() // 2, y=size_canvas_y)
    else:
        t1.configure(bg="red")
        t0.configure(bg="#f0f0f0")
        t0.configure(text="Player №1")
        t0.place(x=size_canvas_x // 2 - t0.winfo_reqwidth() // 2, y=size_canvas_y + 3)
        t1.configure(text="Player №2" + add_to_label)
        t1.place(x=size_canvas_x + menu_x + size_canvas_x // 2 - t1.winfo_reqwidth() // 2, y=size_canvas_y + 3)
        t3.configure(text="Player №1's Turn")
        t3.place(x=size_canvas_x + menu_x // 2 - t3.winfo_reqwidth() // 2, y=size_canvas_y)

mark_player(player_turn_1)

# Function to show Player 1's ships on the canvas
def button_show_enemy1():
    for i in range(0, s_x):
        for j in range(0, s_y):
            if enemy_ships1[j][i] > 0:
                color = "red"
                if points1[j][i] != -1:
                    color = "green"
                _id = canvas.create_rectangle(i * step_x, j * step_y, i * step_x + step_x, j * step_y + step_y,
                                              fill=color)
                list_ids.append(_id)

# Function to show Player 2's ships on the canvas
def button_show_enemy2():
    for i in range(0, s_x):
        for j in range(0, s_y):
            if enemy_ships2[j][i] > 0:
                color = "red"
                if points2[j][i] != -1:
                    color = "green"
                _id = canvas.create_rectangle(size_canvas_x + menu_x + i * step_x, j * step_y,
                                              size_canvas_x + menu_x + i * step_x + step_x, j * step_y + step_y,
                                              fill=color)
                list_ids.append(_id)

# Function to reset the game and start again
def button_begin_again():
    global list_ids
    global points1, points2
    global boom
    global enemy_ships1, enemy_ships2
    for el in list_ids:
        canvas.delete(el)
    list_ids = []
    generate_ships_list()
    enemy_ships1 = generate_enemy_ships()
    enemy_ships2 = generate_enemy_ships()
    points1 = [[-1 for i in range(s_x)] for i in range(s_y)]
    points2 = [[-1 for i in range(s_x)] for i in range(s_y)]
    boom = [[0 for i in range(s_x)] for i in range(s_y)]

# Button to show Player 1's ships
b0 = Button(tk, text="Show Player 1's Ships", command=button_show_enemy1)
b0.place(x=size_canvas_x + menu_x // 2 - b0.winfo_reqwidth() // 2, y=10)

# Button to show Player 2's ships
b1 = Button(tk, text="Show Player 2's Ships", command=button_show_enemy2)
b1.place(x=size_canvas_x + menu_x // 2 - b1.winfo_reqwidth() // 2, y=60)

# Button to restart the game
b2 = Button(tk, text="Restart!", command=button_begin_again)
b2.place(x=size_canvas_x + menu_x // 2 - b2.winfo_reqwidth() // 2, y=110)

# Function to draw a point (hit or miss) for Player 1
def draw_point(x, y):
    if enemy_ships1[y][x] == 0:
        color = "red"
        id1 = canvas.create_oval(x * step_x, y * step_y, x * step_x + step_x, y * step_y + step_y, fill=color)
        id2 = canvas.create_oval(x * step_x + step_x // 3, y * step_y + step_y // 3, x * step_x + step_x - step_x // 3,
                                 y * step_y + step_y - step_y // 3, fill="white")
        list_ids.append(id1)
        list_ids.append(id2)
    if enemy_ships1[y][x] > 0:
        color = "blue"
        id1 = canvas.create_rectangle(x * step_x, y * step_y + step_y // 2 - step_y // 10, x * step_x + step_x,
                                      y * step_y + step_y // 2 + step_y // 10, fill=color)
        id2 = canvas.create_rectangle(x * step_x + step_x // 2 - step_x // 10, y * step_y,
                                      x * step_x + step_x // 2 + step_x // 10, y * step_y + step_y, fill=color)
        list_ids.append(id1)
        list_ids.append(id2)

# Function to draw a point for Player 2
def draw_point2(x, y, offset_x=size_canvas_x + menu_x):
    if enemy_ships2[y][x] == 0:
        color = "red"
        id1 = canvas.create_oval(offset_x + x * step_x, y * step_y, offset_x + x * step_x + step_x, y * step_y + step_y,
                                 fill=color)
        id2 = canvas.create_oval(offset_x + x * step_x + step_x // 3, y * step_y + step_y // 3,
                                 offset_x + x * step_x + step_x - step_x // 3,
                                 y * step_y + step_y - step_y // 3, fill="white")
        list_ids.append(id1)
        list_ids.append(id2)
    if enemy_ships2[y][x] > 0:
        color = "blue"
        id1 = canvas.create_rectangle(offset_x + x * step_x, y * step_y + step_y // 2 - step_y // 10,
                                      offset_x + x * step_x + step_x,
                                      y * step_y + step_y // 2 + step_y // 10, fill=color)
        id2 = canvas.create_rectangle(offset_x + x * step_x + step_x // 2 - step_x // 10, y * step_y,
                                      offset_x + x * step_x + step_x // 2 + step_x // 10, y * step_y + step_y,
                                      fill=color)
        list_ids.append(id1)
        list_ids.append(id2)

# Function to check if Player 1 has won
def check_winner(x, y):
    win = False
    if enemy_ships1[y][x] > 0:
        boom[y][x] = enemy_ships1[y][x]
    sum_enemy_ships1 = sum(sum(i) for i in zip(*enemy_ships1))
    sum_boom = sum(sum(i) for i in zip(*boom))
    if sum_enemy_ships1 == sum_boom:
        win = True
    return win

# Function to check if Player 1 has won
def check_winner2():
    win = True
    for i in range(0, s_x):
        for j in range(0, s_y):
            if enemy_ships1[j][i] > 0:
                if points1[j][i] == -1:
                    win = False
    return win

# Function to check if Player 2 has won
def check_winner2_player2():
    win = True
    for i in range(0, s_x):
        for j in range(0, s_y):
            if enemy_ships2[j][i] > 0:
                if points2[j][i] == -1:
                    win = False
    return win

# Function for the computer's turn (if playing against the computer)
def computer_turn():
    global points1, points2, player_turn_1
    tk.update()
    time.sleep(1)
    player_turn_1 = False
    ip_x = random.randint(0, s_x - 1)
    ip_y = random.randint(0, s_y - 1)
    while not points1[ip_y][ip_x] == -1:
        ip_x = random.randint(0, s_x - 1)
        ip_y = random.randint(0, s_y - 1)
    points1[ip_y][ip_x] = 7
    draw_point(ip_x, ip_y)
    if check_winner2():
        winner = "Player №2 Wins"
        winner_add = "(All of Player №1’s ships are sunk)"
        points1 = [[10 for i in range(s_x)] for i in range(s_y)]
        points2 = [[10 for i in range(s_x)] for i in range(s_y)]
        id1 = canvas.create_rectangle(step_x * 3, step_y * 3, size_canvas_x + menu_x + size_canvas_x - step_x * 3,
                                      size_canvas_y - step_y, fill="blue")
        list_ids.append(id1)
        id2 = canvas.create_rectangle(step_x * 3 + step_x // 2, step_y * 3 + step_y // 2,
                                      size_canvas_x + menu_x + size_canvas_x - step_x * 3 - step_x // 2,
                                      size_canvas_y - step_y - step_y // 2, fill="yellow")
        list_ids.append(id2)
        id3 = canvas.create_text(step_x * 10, step_y * 5, text=winner, font=("Arial", 50), justify=CENTER)
        id4 = canvas.create_text(step_x * 10, step_y * 6, text=winner_add, font=("Arial", 25), justify=CENTER)
        list_ids.append(id3)
        list_ids.append(id4)

# Function to handle mouse click events for both players
def add_to_all(event):
    global points1, points2, player_turn_1
    _type = 0  # Left Click
    if event.num == 3:
        _type = 1  # Right Click
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
    ip_x = mouse_x // step_x
    ip_y = mouse_y // step_y

    # Player 1's field
    if ip_x < s_x and ip_y < s_y and player_turn_1:
        if points1[ip_y][ip_x] == -1:
            points1[ip_y][ip_x] = _type
            player_turn_1 = False
            draw_point(ip_x, ip_y)
            if check_winner2():
                player_turn_1 = True
                winner = "Player №2 Wins"
                winner_add = "(All of Player №1’s ships are sunk)"
                points1 = [[10 for i in range(s_x)] for i in range(s_y)]
                points2 = [[10 for i in range(s_x)] for i in range(s_y)]
                id1 = canvas.create_rectangle(step_x * 3, size_canvas_y // 2, size_canvas_x + menu_x + size_canvas_x - step_x * 3, size_canvas_y // 2 + step_y + step_y // 2 + 50 + 25 + step_y // 2, fill="blue")
                list_ids.append(id1)
                id2 = canvas.create_rectangle(step_x * 3 + step_x // 2, size_canvas_y // 2 + step_y // 2, size_canvas_x + menu_x + size_canvas_x - step_x * 3 - step_x // 2, size_canvas_y // 2 + step_y + step_y // 2 + 50 + 25 + step_y // 2 - step_y // 2, fill="yellow")
                list_ids.append(id2)
                id3 = canvas.create_text(size_canvas_x + menu_x // 2, size_canvas_y // 2 + step_y + step_y // 2, text=winner, font=("Arial", 50), justify=CENTER)
                id4 = canvas.create_text(size_canvas_x + menu_x // 2, size_canvas_y // 2 + step_y + step_y // 2 + 50, text=winner_add, font=("Arial", 25), justify=CENTER)
                list_ids.append(id3)
                list_ids.append(id4)

    # Player 2's field
    if ip_x >= s_x + delta_menu_x and ip_x <= s_x + s_x + delta_menu_x and ip_y < s_y and not player_turn_1:
        if points2[ip_y][ip_x - s_x - delta_menu_x] == -1:
            points2[ip_y][ip_x - s_x - delta_menu_x] = _type
            player_turn_1 = True
            draw_point2(ip_x - s_x - delta_menu_x, ip_y)
            if check_winner2_player2():
                player_turn_1 = False
                winner = "Player №1 Wins"
                winner_add = "(All of Player №2’s ships are sunk)"
                points1 = [[10 for i in range(s_x)] for i in range(s_y)]
                points2 = [[10 for i in range(s_x)] for i in range(s_y)]
                id1 = canvas.create_rectangle(step_x * 3, size_canvas_y // 2, size_canvas_x + menu_x + size_canvas_x - step_x * 3, size_canvas_y // 2 + step_y + step_y // 2 + 50 + 25 + step_y // 2, fill="blue")
                list_ids.append(id1)
                id2 = canvas.create_rectangle(step_x * 3 + step_x // 2, size_canvas_y // 2 + step_y // 2, size_canvas_x + menu_x + size_canvas_x - step_x * 3 - step_x // 2, size_canvas_y // 2 + step_y + step_y // 2 + 50 + 25 + step_y // 2 - step_y // 2, fill="yellow")
                list_ids.append(id2)
                id3 = canvas.create_text(size_canvas_x + menu_x // 2, size_canvas_y // 2 + step_y + step_y // 2, text=winner, font=("Arial", 50), justify=CENTER)
                id4 = canvas.create_text(size_canvas_x + menu_x // 2, size_canvas_y // 2 + step_y + step_y // 2 + 50, text=winner_add, font=("Arial", 25), justify=CENTER)
                list_ids.append(id3)
                list_ids.append(id4)
            elif computer_vs_human:
                mark_player(player_turn_1)
                computer_turn()
    mark_player(player_turn_1)

canvas.bind_all("<Button-1>", add_to_all)  # Left Click
canvas.bind_all("<Button-3>", add_to_all)  # Right Click

# Function to generate the list of ships for both players
def generate_ships_list():
    global ships_list
    ships_list = []
    # generate a list of random ship lengths
    for i in range(0, ships):
        ships_list.append(random.choice([ship_len1, ship_len2, ship_len3]))
    # print(ships_list)

# Function to generate enemy ships
def generate_enemy_ships():
    global ships_list
    enemy_ships = []

    # calculate the total length of ships
    sum_1_all_ships = sum(ships_list)
    sum_1_enemy = 0

    # print("sum: ", sum_1_all_ships)

    while sum_1_enemy != sum_1_all_ships:
        # reset the enemy ship array
        enemy_ships = [[0 for i in range(s_x + 1)] for i in
                       range(s_y + 1)]  # +1 for additional line to the right and bottom, for successful enemy ship generation checks

        for i in range(0, ships):
            len = ships_list[i]
            horizont_vertikal = random.randrange(1, 3)  # 1- horizontal 2- vertical

            primerno_x = random.randrange(0, s_x)
            if primerno_x + len > s_x:
                primerno_x = primerno_x - len

            primerno_y = random.randrange(0, s_y)
            if primerno_y + len > s_y:
                primerno_y = primerno_y - len

            if horizont_vertikal == 1:
                if primerno_x + len <= s_x:
                    for j in range(0, len):
                        try:
                            check_near_ships = 0
                            check_near_ships = enemy_ships[primerno_y][primerno_x - 1] + \
                                               enemy_ships[primerno_y][primerno_x + j] + \
                                               enemy_ships[primerno_y][primerno_x + j + 1] + \
                                               enemy_ships[primerno_y + 1][primerno_x + j + 1] + \
                                               enemy_ships[primerno_y - 1][primerno_x + j + 1] + \
                                               enemy_ships[primerno_y + 1][primerno_x + j] + \
                                               enemy_ships[primerno_y - 1][primerno_x + j]
                            if check_near_ships == 0:  # store if there's nothing nearby
                                enemy_ships[primerno_y][primerno_x + j] = i + 1  # store the ship's number
                        except Exception:
                            pass
            if horizont_vertikal == 2:
                if primerno_y + len <= s_y:
                    for j in range(0, len):
                        try:
                            check_near_ships = 0
                            check_near_ships = enemy_ships[primerno_y - 1][primerno_x] + \
                                               enemy_ships[primerno_y + j][primerno_x] + \
                                               enemy_ships[primerno_y + j + 1][primerno_x] + \
                                               enemy_ships[primerno_y + j + 1][primerno_x + 1] + \
                                               enemy_ships[primerno_y + j + 1][primerno_x - 1] + \
                                               enemy_ships[primerno_y + j][primerno_x + 1] + \
                                               enemy_ships[primerno_y + j][primerno_x - 1]
                            if check_near_ships == 0:  # store if there's nothing nearby
                                enemy_ships[primerno_y + j][primerno_x] = i + 1  # store the ship's number
                        except Exception:
                            pass

        # total count of ships
        sum_1_enemy = 0
        for i in range(0, s_x):
            for j in range(0, s_y):
                if enemy_ships[j][i] > 0:
                    sum_1_enemy = sum_1_enemy + 1

    return enemy_ships


generate_ships_list()
enemy_ships1 = generate_enemy_ships()
enemy_ships2 = generate_enemy_ships()

while app_running:
    if app_running:
        tk.update_idletasks()
        tk.update()
    time.sleep(0.005)