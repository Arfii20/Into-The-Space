# Coursework 2 of COMP16321

"""
*** The screen resolution is 1440x900

* This is a classic asteroid game where the player needs to avoid hitting the asteroids to survive.
* The difficulty increases at certain scores.
* The speed of the asteroids will increase making the game harder and harder at each level.
"""

# game_icon.ico source: https://www.freeiconspng.com/img/17270
# spaceship_image.png source: https://www.pngkey.com/detail/u2q8a9t4r5y3a9r5_spaceship-png-file-spaceship-png/
# asteroid_1.png source: https://www.pngwing.com/en/free-png-yoygi
# asteroid_2.png source: https://pngimg.com/image/105528
# asteroid_3.png source: https://pngimg.com/image/105498
# asteroid_4.png source: https://pngimg.com/image/105494
# main.png: https://www.pngitem.com/middle/wmmbxo_asteroids-asteroid-mining-transparent-background-asteroids-png-png/

# options.png source: http://pixelartmaker.com/art/e996fd04f0c49f2
# start.png source: http://pixelartmaker.com/art/6a45404d913e6d1
# exit.png source: http://pixelartmaker.com/art/36cd392e6295705
# pause.png source: https://www.pixilart.com/draw/pause-button-2-22f5240ce52a5c4
# restart.png source: http://pixelartmaker.com/art/ad99f7494306997
# resume.png source: http://pixelartmaker.com/art/5be181b34875416
# leaderboard.png source: http://pixelartmaker.com/art/7cc98bfa5bbcc0b


from tkinter import Tk, Canvas, Button, Label, Frame
from tkinter.font import Font
from PIL import Image, ImageTk
from random import randint, shuffle
from os import getlogin
from math import sqrt, pow
from time import sleep


# Configure main window
def configure_window():
    window.title("Asteroid Game")
    window.iconbitmap("images/game_icon.ico")

    # Disabled resizing of the window
    window.resizable(False, False)

    """ Fixing geometry so that the window opens at the center """
    # Width and height of the window
    width = window_width
    height = window_height

    # Screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Change of coordinates
    x = int(screen_width / 2 - width / 2)
    y = int(screen_height / 2 - height / 2 - 20)

    # screen position
    window.geometry(f"{width}x{height}+{x}+{y}")


# sets the state of the selected buttons to hidden
def normal_buttons():
    canvas_main.itemconfig(options, state="normal")
    canvas_main.itemconfig(exited, state="normal")
    canvas_main.itemconfig(leaderboards, state="normal")


# sets the state of the selected buttons to hidden
def hidden_buttons():
    canvas_main.itemconfig(exited, state="hidden")
    canvas_main.itemconfig(leaderboards, state="hidden")
    canvas_main.itemconfig(options, state="hidden")


# Moves the buttons up/down the y-axis
def shift_buttons(y):
    canvas_main.coords(resume, resume_coords[0], resume_coords[1] + y)
    canvas_main.coords(restarted, restart_coords[0], restart_coords[1] + y)
    canvas_main.coords(exited, exit_coords[0], exit_coords[1] + y)
    canvas_main.coords(leaderboards, leaderboard_coords[0], leaderboard_coords[1] + y)
    canvas_main.coords(options, options_coords[0], options_coords[1] + y)


def bind_keys():
    canvas_main.bind("<Left>", move_spaceship_left)
    canvas_main.bind("<Right>", move_spaceship_right)
    canvas_main.bind("<Up>", move_spaceship_up)
    canvas_main.bind("<Down>", move_spaceship_down)


def unbind_keys():
    canvas_main.unbind("<Left>")
    canvas_main.unbind("<Right>")
    canvas_main.unbind("<Up>")
    canvas_main.unbind("<Down>")


# Creates the main menu page and buttons
def main_menu(_):
    # Deleting the text
    canvas_main.delete(press_any_key)
    canvas_main.delete(welcome_text)

    # Add buttons to main menu of canvas
    canvas_main.itemconfig(start, state="normal")
    normal_buttons()


# Creating keybindings to move the spaceship
def move_spaceship_left(_):
    canvas_main.move(spaceship, -15, 0)


def move_spaceship_right(_):
    canvas_main.move(spaceship, 15, 0)


def move_spaceship_up(_):
    canvas_main.move(spaceship, 0, -15)


def move_spaceship_down(_):
    canvas_main.move(spaceship, 0, 15)


def game_over_buttons():
    normal_buttons()
    shift_buttons(-30)
    canvas_main.itemconfig(restarted, state="normal")
    canvas_main.delete(game_over_text)


# Creating the pause menu
def pause_menu(_):
    global pause_game

    # pauses the game and adds buttons
    if not pause_game:
        pause_game = True
        canvas_main.itemconfig(main_image, state="normal")

        canvas_main.itemconfig(resume, state="normal")
        canvas_main.itemconfig(restarted, state="normal")
        normal_buttons()

        unbind_keys()

    # unpauses the game and hides buttons
    elif pause_game:
        pause_game = False
        canvas_main.itemconfig(resume, state="hidden")
        canvas_main.itemconfig(restarted, state="hidden")
        canvas_main.itemconfig(main_image, state="hidden")
        hidden_buttons()
        bind_keys()

        # calls the falling function as long as not paused
        asteroid_falling_collision()


# Resumes the game through button click
def resume_button_click():
    global pause_game
    canvas_main.itemconfig(resume, state="hidden")
    canvas_main.itemconfig(restarted, state="hidden")
    canvas_main.itemconfig(main_image, state="hidden")
    hidden_buttons()
    pause_game = False
    asteroid_falling_collision()


def options_button_click():
    pass


def leaderboard():
    leaderboard_frame.pack(fill="both", expand=1)

    # Hides the main menu buttons
    canvas_main.itemconfig(main_image, state="hidden")
    canvas_main.itemconfig(start, state="hidden")
    canvas_main.itemconfig(resume, state="hidden")
    canvas_main.itemconfig(restarted, state="hidden")
    hidden_buttons()

    Label(leaderboard_frame, text="Leaderboard:\n", font=("OCR A Extended", 40),
          bg="black", fg="white").pack(anchor="w", padx=30, pady=(30, 0))

    file = open("leaderboard.txt", "r")
    lines = file.readlines()
    if len(lines) == 0:
        Label(leaderboard_frame, text="Nothing to show here\n", font=("OCR A Extended", 40),
              bg="black", fg="white").pack(anchor="w", padx=30)
    else:
        for idx, val in enumerate(lines, start=1):
            Label(leaderboard_frame, text=(str(idx) + ". " + str(val)), bg="black", fg="white",
                  font=("OCR A Extended", 20)).pack(anchor="w", padx=30)
        Button(leaderboard_frame, text="Click to clear history", command=clear_history).pack()
    file.close()

    Button(leaderboard_frame, text="Click to close", command=leaderboard_clear).pack()


def leaderboard_clear():
    global leaderboard_frame
    leaderboard_frame.pack_forget()
    canvas_main.itemconfig(resume, state="normal")
    canvas_main.itemconfig(start, state="normal")
    normal_buttons()
    canvas_main.itemconfig(main_image, state="normal")


def clear_history():
    pass


#     file = open("History.txt", "w")
#     file.write("")
#     file.close()
#
#     for i in lead
#     label1 = Label(leaderboard_frame1, text="Match History:\n", font=40).pack(anchor="w", padx=20)
#     label2 = Label(leaderboard_frame1, text="Nothing to show here\n", ).pack(anchor="w", padx=20)
#     leaderboard_frame.destroy()
#
#     close = Button(leaderboard_frame1, text="Click to close", command=leaderboard_frame1.destroy).pack()

def add_images():
    global spaceship
    # Add spaceship to canvas
    canvas_main.itemconfig(spaceship, state="normal")


def asteroid_falling_collision():
    global game_over_text, pause_game, game_over, score, asteroid_speed

    canvas_main.itemconfig(Level, )

    while not pause_game:
        y = [asteroid_speed] * 4
        for i in range(4):
            pos = canvas_main.coords(asteroid[i])
            if pos[1] >= window_height:
                canvas_main.coords(asteroid[i], randint(50, window_width - 110), randint(-500, 0))
                score += 10
                score_txt = "Score: " + str(score)
                canvas_main.itemconfig(scoreText, text=score_txt)
                if score != 0 and score % 100 == 0:
                    asteroid_speed += 1
                    canvas_main.itemconfig(Level, state="normal",
                                           text=("Level " + str(asteroid_speed - 3) + ": Speed increased"))
                elif (score - 40) % 100 == 0:
                    canvas_main.itemconfig(Level, state="hidden")

            asteroid_pos = canvas_main.coords(asteroid[i])
            spaceship_pos = canvas_main.coords(spaceship)

            # Collision detection
            game_over = 110 > sqrt(pow(asteroid_pos[0] - spaceship_pos[0], 2)
                                   + pow(asteroid_pos[1] - spaceship_pos[1], 2))

            # Game over
            if game_over:
                unbind_keys()
                canvas_main.unbind("<Escape>")
                game_over_text = canvas_main.create_text(window_width / 2, window_height / 2, fill="white",
                                                         font=("OCR A Extended", 120), text="Game Over")
                canvas_main.after(1000, game_over_buttons)
                break
            canvas_main.move(asteroid[i], 0, y[i])
        if not game_over:
            sleep(0.0001)
            window.update()
            continue
        break


def restart_game():
    global restart_flag, pause_game, asteroid_speed
    pause_game = False
    restart_flag = True
    asteroid_speed = 4
    canvas_main.itemconfig(resume, state="hidden")
    canvas_main.itemconfig(restarted, state="hidden")
    canvas_main.itemconfig(Level, text="      Level " + str(asteroid_speed - 3) + "\n\nDodge the Asteroids")
    for j in asteroid:
        canvas_main.delete(j)
    hidden_buttons()
    main_game()


# Creating main game function
def main_game():
    global score, scoreText, restart_flag, asteroid

    canvas_main.unbind("<Return>")
    shift_buttons(50)

    # Hides the main menu buttons
    canvas_main.itemconfig(main_image, state="hidden")
    canvas_main.itemconfig(start, state="hidden")
    hidden_buttons()

    # Deletes the scoreText when restarting
    if restart_flag:
        canvas_main.delete(scoreText)
        restart_flag = False

    # Adding all the images
    add_images()

    """ Keybindings """
    bind_keys()
    canvas_main.bind("<Escape>", pause_menu)
    canvas_main.focus_set()

    """ Making the scoring system """
    # storing and displaying the score
    score = 0
    score_text = "Score: " + str(score)

    # displaying the score on the top right
    scoreText = canvas_main.create_text(window_width - window_width / 8, window_height / 15,
                                        fill="white", font=("OCR A Extended", 30), text=score_text)
    canvas_main.focus(score_text)

    asteroid = []
    for _ in range(4):
        asteroid_x = randint(50, window_width - 110)
        asteroid_y = randint(-1000, -100)
        asteroid_select = randint(0, 3)
        asteroid.append(canvas_main.create_image(asteroid_x, asteroid_y,
                                                 image=asteroid_image[asteroid_select],
                                                 anchor="nw"))
    canvas_main.itemconfig(Level, state="normal")
    asteroid_falling_collision()


window = Tk()

"""Defining variables"""
# Width and height of the window
window_width = 1440
window_height = 900

configure_window()

# Variables
pause_game = False
restart_flag = False
score = 0
asteroid_speed = 4

""" Creating the Canvas """
canvas_main = Canvas(window, width=window_width, height=window_height, bg="black")
canvas_main.pack(fill="both", expand=True)

""" Creating the leaderboard frame """
leaderboard_frame = Frame(canvas_main, width=window_width, height=window_height, bg="black")

"""Adding Background to the main game"""
color = ["white", "#fefefe", "#dfdfdf", "#ad7f00", "#828181"]

# Adding 300 starts to reduce lag
for _ in range(300):
    bg_x = randint(0, window_width)
    bg_y = randint(0, window_height)

    size = randint(1, 5)
    color_chooser = randint(0, 4)

    canvas_main.create_oval(bg_x, bg_y, bg_x + size, bg_y + size, fill=color[color_chooser])

# Level text that will be shown upon each level
Level = canvas_main.create_text(window_width / 2, window_height / 10, fill="white", font=("OCR A Extended", 25),
                                text=("      Level " + str(asteroid_speed - 3) + "\n\nDodge the Asteroids"))

canvas_main.itemconfig(Level, state="hidden")
""" Start menu """
# main menu image
main_menu_image = ImageTk.PhotoImage(Image.open("images/main.png"))
main_image = canvas_main.create_image(window_width / 2, window_height / 2,
                                      image=main_menu_image, anchor="center")
canvas_main.itemconfig(main_image, state="normal")

welcome_text = canvas_main.create_text(window_width / 2, window_height / 2 - 30,
                                       fill="white", font=("OCR A Extended", 40),
                                       text="Hello " + str(getlogin()))

# Press any key to continue to start menu
press_any_key = canvas_main.create_text(window_width / 2, window_height / 2 + 30,
                                        fill="white", font=("OCR A Extended", 25),
                                        text="Please press enter to continue")

""" Start button """
start_org = Image.open("images/start.png")
start_resized = start_org.resize((200, 75), Image.Resampling.LANCZOS)
start_image = ImageTk.PhotoImage(start_resized)
start_button = Button(window, image=start_image, bg="black", border=0, command=main_game)
start = canvas_main.create_window(window_width / 2, window_height / 2 - 165, window=start_button)
canvas_main.itemconfig(start, state="hidden")
start_coords = canvas_main.coords(start)

""" options button """
options_org = Image.open("images/options.png")
options_resized = options_org.resize((240, 75), Image.Resampling.LANCZOS)
options_image = ImageTk.PhotoImage(options_resized)
options_button = Button(window, image=options_image, bg="black", border=0, command=options_button_click)
options = canvas_main.create_window(window_width / 2, window_height / 2 + 55, window=options_button)
canvas_main.itemconfig(options, state="hidden")
options_coords = canvas_main.coords(options)

""" exit button """
exit_org = Image.open("images/exit.png")
exit_resized = exit_org.resize((200, 70), Image.Resampling.LANCZOS)
exit_image = ImageTk.PhotoImage(exit_resized)
exit_button = Button(window, image=exit_image, bg="black", border=0, command=window.destroy)
exited = canvas_main.create_window(window_width / 2, window_height / 2 + 165, window=exit_button)
canvas_main.itemconfig(exited, state="hidden")
exit_coords = canvas_main.coords(exited)

""" resume button """
resume_org = Image.open("images/resume.png")
resume_resized = resume_org.resize((244, 80), Image.Resampling.LANCZOS)
resume_image = ImageTk.PhotoImage(resume_resized)
resume_button = Button(window, image=resume_image, border=0, bg="black", command=resume_button_click)
resume = canvas_main.create_window(window_width / 2, window_height / 2 - 275, window=resume_button)
canvas_main.itemconfig(resume, state="hidden")
resume_coords = canvas_main.coords(resume)

""" restart button """
restart_org = Image.open("images/restart.png")
restart_resized = restart_org.resize((244, 80), Image.Resampling.LANCZOS)
restart_image = ImageTk.PhotoImage(restart_resized)
restart_button = Button(window, image=restart_image, border=0, bg="black", command=restart_game)
restarted = canvas_main.create_window(window_width / 2, window_height / 2 - 165, window=restart_button)
canvas_main.itemconfig(restarted, state="hidden")
restart_coords = canvas_main.coords(restarted)

""" leaderboard button """
leaderboard_org = Image.open("images/leaderboard.png")
leaderboard_resized = leaderboard_org.resize((474, 80), Image.Resampling.LANCZOS)
leaderboard_image = ImageTk.PhotoImage(leaderboard_resized)
leaderboard_button = Button(window, image=leaderboard_image, border=0, bg="black", command=leaderboard)
leaderboards = canvas_main.create_window(window_width / 2, window_height / 2 - 55, window=leaderboard_button)
canvas_main.itemconfig(leaderboards, state="hidden")
leaderboard_coords = canvas_main.coords(leaderboards)

""" Spaceship """
spaceship_org = Image.open("images/spaceship_image.png")
spaceship_resized = spaceship_org.resize((100, 100), Image.Resampling.LANCZOS)
spaceship_image = ImageTk.PhotoImage(spaceship_resized)
spaceship = canvas_main.create_image(window_width / 2 - 40,
                                     window_height - window_height / 6,
                                     image=spaceship_image, anchor="nw")
canvas_main.itemconfig(spaceship, state="hidden")

""" List data structure to store asteroid images """
asteroid_image = []
for m in range(1, 5):
    asteroid_org = Image.open("images/asteroid_" + str(m) + ".png")
    asteroid_resized = asteroid_org.resize((120, 120), Image.Resampling.LANCZOS)
    asteroid_image.append(ImageTk.PhotoImage(asteroid_resized))

canvas_main.bind("<Return>", main_menu)
canvas_main.focus_set()

window.mainloop()
