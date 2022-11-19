# Coursework 2 of COMP16321

"""
*** The screen resolution is 1440x900

* This is a classic asteroid game where the player needs to avoid hitting the asteroids to survive.
* The difficulty increases at certain scores.
* The speed of the asteroids will increase making the game harder and harder at each level.
"""

# Image sources

# game_icon.ico source: https://www.freeiconspng.com/img/17270
# spaceship_image.png source: https://www.pngkey.com/detail/u2q8a9t4r5y3a9r5_spaceship-png-file-spaceship-png/
# asteroid_1.png source: https://www.pngwing.com/en/free-png-yoygi
# asteroid_2.png source: https://pngimg.com/image/105528
# asteroid_3.png source: https://pngimg.com/image/105498
# asteroid_4.png source: https://pngimg.com/image/105494
# main.png: https://www.pngitem.com/middle/wmmbxo_asteroids-asteroid-mining-transparent-background-asteroids-png-png/
# spreadsheet: https://upload.wikimedia.org/wikipedia/commons/2/25/LibreOffice_7.2.4.1_Calc_with_csv_screenshot.png

# options.png source: http://pixelartmaker.com/art/e996fd04f0c49f2
# start.png source: http://pixelartmaker.com/art/6a45404d913e6d1
# exit.png source: http://pixelartmaker.com/art/36cd392e6295705
# pause.png source: https://www.pixilart.com/draw/pause-button-2-22f5240ce52a5c4
# restart.png source: http://pixelartmaker.com/art/ad99f7494306997
# resume.png source: http://pixelartmaker.com/art/5be181b34875416
# leaderboard.png source: http://pixelartmaker.com/art/7cc98bfa5bbcc0b
# back.png source: http://pixelartmaker.com/art/fe696dcfb337a49
# load.png source: http://pixelartmaker.com/art/84432c853ed5006
# save.png source: http://pixelartmaker.com/art/154309787c95a2f
# cheat.png source: http://pixelartmaker.com/art/184effceebac6a0
# help.png source: http://pixelartmaker.com/art/e423fd17591bcaa

from tkinter import Tk, Canvas, Button, Label, Frame, ttk
from tkinter.font import Font
from PIL import Image, ImageTk
from random import randint, shuffle
from os import getlogin
from math import sqrt, pow
from time import sleep
from pickle import dump as dmp, load as ld
from webbrowser import open as opn


def configure_window():
    """
    Adds title, icon and fixes the size of the main window
    Makes the main window not resizable to minimise complexity.
    Fixes the geometry such that the window is always opened at the center.
    """
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


def unbind_keys():
    """
    Unbinds the movement keys of the spaceship
    """
    canvas_main.unbind("<Left>")
    canvas_main.unbind("<Right>")
    canvas_main.unbind("<Up>")
    canvas_main.unbind("<Down>")
    canvas_main.unbind("<Shift-Z>")
    canvas_main.unbind("<Shift-X>")
    canvas_main.unbind("<Shift-C>")
    canvas_main.unbind("<Shift-V>")


def bind_keys():
    """
    Binds the movement keys of the spaceship
    """
    canvas_main.bind("<Left>", move_spaceship_left)
    canvas_main.bind("<Right>", move_spaceship_right)
    canvas_main.bind("<Up>", move_spaceship_up)
    canvas_main.bind("<Down>", move_spaceship_down)
    canvas_main.bind("<Shift-Z>", cheatz_reduce_speed_default)
    canvas_main.bind("<Shift-X>", cheatx_reduce_speed_by_one)
    canvas_main.bind("<Shift-C>", cheatc_increase_score)
    canvas_main.bind("<Shift-V>", cheatv_invulnerability)


def move_spaceship_left(_):
    """
    Moves spaceship left 15 pixels everytime it is called
    """

    canvas_main.move(spaceship, -15, 0)


def move_spaceship_right(_):
    """
    Moves spaceship right 15 pixels everytime it is called
    """
    canvas_main.move(spaceship, 15, 0)


def move_spaceship_up(_):
    """
    Moves spaceship up 15 pixels everytime it is called
    """
    canvas_main.move(spaceship, 0, -15)


def move_spaceship_down(_):
    """
    Moves spaceship down 15 pixels everytime it is called
    """
    canvas_main.move(spaceship, 0, 15)


def spaceship_touches_sides():
    """
    This function unbinds movement of the spaceship if it touches the sides.
    When the player tries to go other direction, it binds the keys again.
    """
    # Unbinds if touches
    if spaceship_pos[0] > window_width - 100:
        canvas_main.unbind("<Right>")
    if spaceship_pos[0] < 0:
        canvas_main.unbind("<Left>")
    if spaceship_pos[1] > window_height - 100:
        canvas_main.unbind("<Down>")
    if spaceship_pos[1] < 0:
        canvas_main.unbind("<Up>")

    # Binds if goes other direction
    if spaceship_pos[0] < window_width - 100:
        canvas_main.bind("<Right>", move_spaceship_right)
    if spaceship_pos[0] > 0:
        canvas_main.bind("<Left>", move_spaceship_left)
    if spaceship_pos[1] < window_height - 100:
        canvas_main.bind("<Down>", move_spaceship_down)
    if spaceship_pos[1] < 0:
        canvas_main.bind("<Up>", move_spaceship_up)


def cheatz_reduce_speed_default(_):
    """
    When pressed Shift+Z the speed is set to 4
    """
    global asteroid_speed
    asteroid_speed = 4
    canvas_main.itemconfig(cheat, state="normal", text="Spead set to default")
    canvas_main.tag_raise(cheat)


def cheatx_reduce_speed_by_one(_):
    """
     When pressed Shift+X the speed is reduced by 1
     """
    global asteroid_speed
    if asteroid_speed > 4:
        asteroid_speed -= 1
    canvas_main.itemconfig(cheat, state="normal", text="Spead reduced by 1")
    canvas_main.tag_raise(cheat)


def cheatc_increase_score(_):
    """
     When pressed Shift+C the score will increase by 500
     """
    global score
    score += 500
    canvas_main.itemconfig(cheat, state="normal", text="Score increased by 500")
    canvas_main.tag_raise(cheat)


def cheatv_invulnerability(_):
    """
    When pressed Shift+V the collision detection will be turned off and on
    """
    global invulnerable
    if not invulnerable:
        invulnerable = True
        canvas_main.itemconfig(cheat, state="normal", text="Invulnerability On")
        canvas_main.tag_raise(cheat)
    elif invulnerable:
        invulnerable = False
        canvas_main.itemconfig(cheat, state="normal", text="Invulnerability Off")
        canvas_main.tag_raise(cheat)


def boss_key(_):
    """
    When tab is clicked, it opens the boss.css file.
    It also pauses the game and shows all the buttons.
    """
    global pause_game
    opn("boss.css")

    pause_game = True
    normal_buttons()
    canvas_main.itemconfig(resume, state="normal")
    canvas_main.itemconfig(restarted, state="normal")
    canvas_main.itemconfig(save, state="normal")
    canvas_main.itemconfig(level, state="hidden")
    canvas_main.itemconfig(cheat, state="hidden")


def hidden_buttons():
    """
    Hides the exit, leaderboard and options buttons
    """
    canvas_main.itemconfig(exited, state="hidden")
    canvas_main.itemconfig(leaderboards, state="hidden")
    canvas_main.itemconfig(options, state="hidden")


def normal_buttons():
    """
    Makes the exit, leaderboard and options buttons visible again
    """
    canvas_main.itemconfig(options, state="normal")
    canvas_main.itemconfig(exited, state="normal")
    canvas_main.itemconfig(leaderboards, state="normal")


def shift_buttons(y):
    """
    Used for changing the button positions along the y-axis
    """
    canvas_main.coords(resume, resume_coords[0], resume_coords[1] + y)
    canvas_main.coords(restarted, restart_coords[0], restart_coords[1] + y)
    canvas_main.coords(exited, exit_coords[0], exit_coords[1] + y)
    canvas_main.coords(leaderboards, leaderboard_coords[0], leaderboard_coords[1] + y)
    canvas_main.coords(options, options_coords[0], options_coords[1] + y)


def game_over_buttons():
    """
    When the game is over, this function is called and it displays all the buttons again.
    """
    normal_buttons()
    canvas_main.itemconfig(game_over_score, state="normal", text="Score: " + str(score))
    canvas_main.tag_raise(game_over_score)
    canvas_main.itemconfig(restarted, state="normal")
    canvas_main.itemconfig(load, state="normal")
    canvas_main.coords(load, window_width / 2, window_height / 2 - 50)
    canvas_main.delete(game_over_text)


def main_menu(_):
    """
    This function removes the welcome screen and displays all the buttons.
    """
    # Deleting the text
    canvas_main.delete(press_any_key)
    canvas_main.delete(welcome_text)

    # Unbinds the enter button from first screen
    canvas_main.unbind("<Return>")

    # Add buttons to main menu of canvas
    canvas_main.itemconfig(start, state="normal")
    canvas_main.itemconfig(load, state="normal")

    normal_buttons()


def pause_menu(_):
    """
    When escape is clicked, the game is paused which stop everything and displays all the buttons
    When escape is clicked again, the game removes buttons and continues the game.
    """
    global pause_game

    # pauses the game and adds buttons
    if not pause_game:
        pause_game = True
        canvas_main.itemconfig(main_image, state="normal")

        canvas_main.itemconfig(resume, state="normal")
        canvas_main.itemconfig(restarted, state="normal")
        canvas_main.itemconfig(save, state="normal")
        canvas_main.itemconfig(level, state="hidden")
        canvas_main.itemconfig(cheat, state="hidden")
        normal_buttons()

        unbind_keys()

    # unpauses the game and hides buttons
    elif pause_game:
        pause_game = False
        canvas_main.itemconfig(resume, state="hidden")
        canvas_main.itemconfig(restarted, state="hidden")
        canvas_main.itemconfig(save, state="hidden")
        canvas_main.itemconfig(main_image, state="hidden")
        canvas_main.itemconfig(level, state="normal")
        hidden_buttons()
        bind_keys()

        # calls the falling function as long as not paused
        asteroids_and_collision()


def resume_button_click():
    """
    When resume button is clicked, clears the buttons from the screen and resumes all the processes
    """
    global pause_game
    canvas_main.itemconfig(resume, state="hidden")
    canvas_main.itemconfig(restarted, state="hidden")
    canvas_main.itemconfig(save, state="hidden")
    canvas_main.itemconfig(main_image, state="hidden")
    hidden_buttons()
    bind_keys()
    pause_game = False
    asteroids_and_collision()


def restart_game():
    """
    When restart button is clicked, this function clears all the items and
    launches the main game function which starts the game from beginning.
    """
    global restart_flag, pause_game, score, asteroid_speed, level_number
    pause_game = False
    restart_flag = True
    asteroid_speed = 4
    level_number = 1
    score = 0

    if score != 0:
        file = open("leaderboard.txt", "a")
        file.write("\n" + str(score))
        file.close()

    canvas_main.itemconfig(resume, state="hidden")
    canvas_main.itemconfig(restarted, state="hidden")
    canvas_main.itemconfig(game_over_score, state="hidden")
    canvas_main.itemconfig(save, state="hidden")
    canvas_main.itemconfig(level, text="      Level " + str(level_number) + "\n\nDodge the Asteroids")
    canvas_main.coords(spaceship, window_width / 2 - 40, window_height - window_height / 6)
    for j in asteroid:
        canvas_main.delete(j)
    hidden_buttons()
    main_game()


def leaderboard():
    """
    Makes the leaderboard which displays the top 10 scores in descending order.
    Hides all the previous widgets and uses file handling to sort and display scores.
    """
    # Packing the outer leaderboard frame
    secondary_frame.pack(fill="both", expand=1)

    # Creating a canvas for the leaderboard
    canvas_leaderboard = Canvas(secondary_frame, bg="black", border=0)
    canvas_leaderboard.pack(side="left", fill="both", expand=1)

    # Creating a scrollbar for the leaderboard
    leaderboard_scrollbar = ttk.Scrollbar(secondary_frame, orient="vertical", command=canvas_leaderboard.yview)
    leaderboard_scrollbar.pack(side="right", fill="y")

    " configure the leaderboard canvas "
    canvas_leaderboard.configure(yscrollcommand=leaderboard_scrollbar.set)
    canvas_leaderboard.bind("<Configure>",
                            lambda e: canvas_leaderboard.configure(scrollregion=canvas_leaderboard.bbox("all")))

    # Creating the main leaderboard frame
    leaderboard_frame = Frame(canvas_leaderboard, width=window_width, height=window_height, bg="black", border=0)
    canvas_leaderboard.create_window((0, 0), window=leaderboard_frame, anchor="nw")

    # Hides the main menu buttons
    canvas_main.itemconfig(main_image, state="hidden")
    canvas_main.itemconfig(start, state="hidden")
    canvas_main.itemconfig(load, state="hidden")
    canvas_main.itemconfig(resume, state="hidden")
    canvas_main.itemconfig(save, state="hidden")
    canvas_main.itemconfig(restarted, state="hidden")
    hidden_buttons()

    Label(leaderboard_frame, text="Leaderboard:\n", font=("OCR A Extended", 35),
          bg="black", fg="white").pack(anchor="w", padx=50, pady=(40, 0))

    unsorted = open("leaderboard.txt", "r")
    words = unsorted.readlines()
    for idx, val in enumerate(words):
        if "\n" in val:
            words[idx] = val[0:len(val) - 1]
    if "" in words:
        words.remove("")
    words = [int(x) for x in words]
    unsorted.close()

    words.sort(reverse=True)

    file_sorted = open("leaderboardsorted.txt", "w")
    for i in words:
        file_sorted.write(str(i) + "\n")
    file_sorted.close()

    file = open("leaderboardsorted.txt", "r")
    lines = file.readlines()
    if len(lines) == 0:
        Label(leaderboard_frame, text="Nothing to show here\n", font=("OCR A Extended", 25),
              bg="black", fg="white").pack(anchor="w", padx=50)
    else:
        count = 1
        for idx, val in enumerate(lines, start=1):
            if count <= 10:
                Label(leaderboard_frame, text=(str(idx) + ". " + str(val)), bg="black", fg="white",
                      font=("OCR A Extended", 20)).pack(anchor="w", padx=50)
                count += 1
    file.close()

    canvas_main.itemconfig(backs, state="normal")


def options_button_click():
    global canvas_options
    # Packing the outer leaderboard frame
    secondary_frame.pack(fill="both", expand=1)

    # Creating a canvas for the leaderboard
    canvas_options = Canvas(secondary_frame, bg="black", border=0)
    canvas_options.pack(side="left", fill="both", expand=1)

    # Adding 300 starts to reduce lag
    for _ in range(300):
        optionsbg_x = randint(0, window_width)
        optionsbg_y = randint(0, window_height)

        options_size = randint(1, 5)
        options_color_chooser = randint(0, 4)

        canvas_options.create_oval(optionsbg_x, optionsbg_y, optionsbg_x + options_size, optionsbg_y + options_size,
                                   fill=color[options_color_chooser])

    # Hides the main menu buttons
    canvas_main.itemconfig(main_image, state="hidden")
    canvas_main.itemconfig(start, state="hidden")
    canvas_main.itemconfig(load, state="hidden")
    canvas_main.itemconfig(resume, state="hidden")
    canvas_main.itemconfig(save, state="hidden")
    canvas_main.itemconfig(restarted, state="hidden")
    hidden_buttons()

    canvas_main.itemconfig(cheats, state="normal")
    canvas_main.itemconfig(helps, state="normal")
    canvas_main.itemconfig(backs, state="normal")


def cheat_codes():
    """ Cheat Codes """
    global cheat_code
    cheat_code_text = "Reset asteroid speed to default:\nShift + z \n\n" \
                      "Reduce asteroid speed by 1:\nShift + x \n\n" \
                      "Increase score by 500:\nShift + c \n\n" \
                      "God Mode (Invulnerability):\nShift + v"

    cheat_code = canvas_options.create_text(window_width / 2, window_height / 3 + 100, fill="white",
                                         font=("OCR A Extended", 25), text=cheat_code_text, justify="center")

    canvas_main.itemconfig(cheats, state="hidden")
    canvas_main.itemconfig(helps, state="hidden")
    canvas_main.itemconfig(backs, state="hidden")

    canvas_main.itemconfig(back1s, state="normal")
    canvas_main.itemconfig(cheat_code, state="normal")
    canvas_main.tag_raise(cheat_code)


def help_player():
    pass


def back_clear_to_options():
    canvas_main.itemconfig(cheats, state="normal")
    canvas_main.itemconfig(helps, state="normal")
    canvas_main.itemconfig(backs, state="normal")

    canvas_main.itemconfig(back1s, state="hidden")
    canvas_options.delete(cheat_code)

def back_clear():
    """
    Clears the screen and brings out the buttons after exit is clicked on.
    Configured for 3 different cases as leaderboard can be accessed from 3 places.
    """
    global secondary_frame
    for widget in secondary_frame.winfo_children():
        widget.destroy()
    canvas_main.itemconfig(cheats, state="hidden")
    canvas_main.itemconfig(helps, state="hidden")
    canvas_main.itemconfig(backs, state="hidden")
    secondary_frame.pack_forget()
    if pause_game:
        canvas_main.itemconfig(resume, state="normal")
        canvas_main.itemconfig(save, state="normal")
        canvas_main.itemconfig(restarted, state="normal")
    elif game_over:
        game_over_buttons()
        canvas_main.coords(load, window_width / 2, window_height / 2 - 50)
    else:
        canvas_main.itemconfig(start, state="normal")
        canvas_main.itemconfig(load, state="normal")
    normal_buttons()
    canvas_main.itemconfig(main_image, state="normal")


def asteroids_and_collision():
    """
    Keeps the asteroid falling loop running till the game is over.
    The collision detection and finds when game over.
    """
    global game_over_text, pause_game, game_over, score, \
        asteroid_speed, spaceship_pos, level_number, invulnerable

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
                    level_number += 1
                    canvas_main.itemconfig(level, state="normal",
                                           text=("Level " + str(level_number) + ": Speed increased"))
                    canvas_main.itemconfig(cheat, state="hidden")
                elif (score - 40) % 100 == 0:
                    canvas_main.itemconfig(level, state="hidden")
                    canvas_main.itemconfig(cheat, state="hidden")

            asteroid_pos = canvas_main.coords(asteroid[i])
            spaceship_pos = canvas_main.coords(spaceship)

            spaceship_touches_sides()

            if not invulnerable:
                # Collision detection
                game_over = 110 > sqrt(pow(asteroid_pos[0] - spaceship_pos[0], 2)
                                       + pow(asteroid_pos[1] - spaceship_pos[1], 2))

                # Game over
                if game_over:
                    unbind_keys()
                    canvas_main.unbind("<Escape>")
                    game_over_text = canvas_main.create_text(window_width / 2, window_height / 2, fill="white",
                                                             font=("OCR A Extended", 120), text="Game Over")
                    canvas_main.itemconfig(level, state="hidden")
                    canvas_main.itemconfig(cheat, state="hidden")
                    canvas_main.itemconfig(scoreText, state="hidden")
                    canvas_main.coords(load, window_width / 2, window_height / 2 - 100)

                    if score != 0:
                        file = open("leaderboard.txt", "a")
                        file.write("\n" + str(score))
                        file.close()

                    canvas_main.after(1000, game_over_buttons)
                    break
            canvas_main.move(asteroid[i], 0, y[i])
        if not game_over:
            sleep(0.0001)
            window.update()
            continue
        break


def main_game():
    """
    Initiates all the widgets and starts the main game.
    Hides the previous buttons and binds the keys to control the spaceship.
    Initials scoring system and asteroid's initial position.
    """
    global score, scoreText, restart_flag, asteroid

    shift_buttons(50)

    # Display only if the game starts from 0
    if score == 0:
        canvas_main.itemconfig(level, text=("      Level " + str(level_number) + "\n\nDodge the Asteroids"))

    # Hides the main menu buttons
    canvas_main.itemconfig(main_image, state="hidden")
    canvas_main.itemconfig(start, state="hidden")
    canvas_main.itemconfig(load, state="hidden")
    hidden_buttons()

    # Deletes the scoreText when restarting
    if restart_flag:
        canvas_main.delete(scoreText)
        restart_flag = False

    # Adding all the images
    canvas_main.itemconfig(spaceship, state="normal")

    """ Keybindings """
    bind_keys()
    canvas_main.bind("<Escape>", pause_menu)

    # Boss Key TAB
    canvas_main.bind("<Tab>", boss_key)
    canvas_main.focus_set()

    """ Making the scoring system """
    # storing and displaying the score
    score_text = "Score: " + str(score)

    # displaying the score on the top right
    scoreText = canvas_main.create_text(window_width - window_width / 8, window_height / 15,
                                        fill="white", font=("OCR A Extended", 30), text=score_text)
    canvas_main.focus(score_text)

    """ Stores the initial asteroid positions to a list """
    asteroid = []
    for _ in range(4):
        asteroid_x = randint(50, window_width - 110)
        asteroid_y = randint(-1000, -100)
        asteroid_select = randint(0, 3)
        asteroid.append(canvas_main.create_image(asteroid_x, asteroid_y,
                                                 image=asteroid_image[asteroid_select],
                                                 anchor="nw"))
    canvas_main.itemconfig(level, state="normal")
    asteroids_and_collision()


def save_game():
    """
    Saves the score, speed and spaceship position for the player to load later.
    Unfortunately this does not save the asteroid positions
    """
    global score, asteroid_speed, spaceship_pos, level_number

    dmp(score, open("save/score.bat", "wb"))
    dmp(asteroid_speed, open("save/asteroid_speed.bat", "wb"))
    dmp(level_number, open("save/level.bat", "wb"))
    dmp(spaceship_pos, open("save/spaceship_pos.bat", "wb"))


def load_game():
    """
    Loads the game from last saved files and resets the on-screen widgets.
    It loads everything apart from the asteroids from last session.
    The asteroids are newly formed after this load.
    """
    global score, asteroid_speed, restart_flag, pause_game, game_over, level_number

    score = ld(open("save/score.bat", "rb"))
    asteroid_speed = ld(open("save/asteroid_speed.bat", "rb"))
    level_number = ld(open("save/level.bat", "rb"))

    ship_pos = ld(open("save/spaceship_pos.bat", "rb"))
    canvas_main.coords(spaceship, ship_pos[0], ship_pos[1])

    canvas_main.itemconfig(load, state="hidden")
    canvas_main.itemconfig(restarted, state="hidden")
    canvas_main.itemconfig(game_over_score, state="hidden")

    if game_over:
        for j in asteroid:
            canvas_main.delete(j)
    hidden_buttons()
    main_game()


window = Tk()

"""Defining variables"""
# Width and height of the window
window_width = 1440
window_height = 900

configure_window()

# Variables
pause_game = False
restart_flag = False
game_over = False
invulnerable = False
score = 0
asteroid_speed = 4
level_number = 1

""" Creating the Canvas """
canvas_main = Canvas(window, width=window_width, height=window_height, bg="black")
canvas_main.pack(fill="both", expand=True)

""" Creating a leaderboard with a scrollbar """
# There is an outer frame to contain a canvas which will contain another frame
secondary_frame = Frame(canvas_main)

""" Score display after game over """
game_over_score = canvas_main.create_text(window_width / 2, window_height / 5, fill="white",
                                          font=("OCR A Extended", 60))
canvas_main.itemconfig(game_over_score, state="hidden")

""" Cheats Message """
cheat = canvas_main.create_text(window_width / 2, window_height / 2, fill="white",
                                font=("OCR A Extended", 20))
canvas_main.itemconfig(cheat, state="hidden")

"""Adding Background to the main game"""
# Color palette
color = ["white", "#fefefe", "#dfdfdf", "#ad7f00", "#828181"]

# Adding 300 starts to reduce lag
for _ in range(300):
    bg_x = randint(0, window_width)
    bg_y = randint(0, window_height)

    size = randint(1, 5)
    color_chooser = randint(0, 4)

    canvas_main.create_oval(bg_x, bg_y, bg_x + size, bg_y + size, fill=color[color_chooser])

# level_number text that will be shown upon each level
level = canvas_main.create_text(window_width / 2, window_height / 7, fill="white", font=("OCR A Extended", 25))
canvas_main.itemconfig(level, state="hidden")

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

"""
The next sections are about loading, resizing and storing images to variables.
Using the images, buttons are created and set the state to hidden to use later.
Position of the buttons are fixed using the coords function
"""

""" Start button """
start_org = Image.open("images/start.png")
start_resized = start_org.resize((200, 75), Image.Resampling.LANCZOS)
start_image = ImageTk.PhotoImage(start_resized)
start_button = Button(window, image=start_image, bg="black", border=0, command=main_game)
start = canvas_main.create_window(window_width / 2, window_height / 2 - 200, window=start_button)
canvas_main.itemconfig(start, state="hidden")
start_coords = canvas_main.coords(start)

""" options button """
options_org = Image.open("images/options.png")
options_resized = options_org.resize((240, 75), Image.Resampling.LANCZOS)
options_image = ImageTk.PhotoImage(options_resized)
options_button = Button(window, image=options_image, bg="black", border=0, command=options_button_click)
options = canvas_main.create_window(window_width / 2, window_height / 2 + 100, window=options_button)
canvas_main.itemconfig(options, state="hidden")
options_coords = canvas_main.coords(options)

""" exit button """
exit_org = Image.open("images/exit.png")
exit_resized = exit_org.resize((200, 70), Image.Resampling.LANCZOS)
exit_image = ImageTk.PhotoImage(exit_resized)
exit_button = Button(window, image=exit_image, bg="black", border=0, command=window.destroy)
exited = canvas_main.create_window(window_width / 2, window_height / 2 + 200, window=exit_button)
canvas_main.itemconfig(exited, state="hidden")
exit_coords = canvas_main.coords(exited)

""" resume button """
resume_org = Image.open("images/resume.png")
resume_resized = resume_org.resize((244, 80), Image.Resampling.LANCZOS)
resume_image = ImageTk.PhotoImage(resume_resized)
resume_button = Button(window, image=resume_image, border=0, bg="black", command=resume_button_click)
resume = canvas_main.create_window(window_width / 2, window_height / 2 - 300, window=resume_button)
canvas_main.itemconfig(resume, state="hidden")
resume_coords = canvas_main.coords(resume)

""" restart button """
restart_org = Image.open("images/restart.png")
restart_resized = restart_org.resize((244, 80), Image.Resampling.LANCZOS)
restart_image = ImageTk.PhotoImage(restart_resized)
restart_button = Button(window, image=restart_image, border=0, bg="black", command=restart_game)
restarted = canvas_main.create_window(window_width / 2, window_height / 2 - 200, window=restart_button)
canvas_main.itemconfig(restarted, state="hidden")
restart_coords = canvas_main.coords(restarted)

""" leaderboard button """
leaderboard_org = Image.open("images/leaderboard.png")
leaderboard_resized = leaderboard_org.resize((474, 80), Image.Resampling.LANCZOS)
leaderboard_image = ImageTk.PhotoImage(leaderboard_resized)
leaderboard_button = Button(window, image=leaderboard_image, border=0, bg="black", command=leaderboard)
leaderboards = canvas_main.create_window(window_width / 2, window_height / 2, window=leaderboard_button)
canvas_main.itemconfig(leaderboards, state="hidden")
leaderboard_coords = canvas_main.coords(leaderboards)

""" save button """
save_org = Image.open("images/save.png")
save_resized = save_org.resize((204, 80), Image.Resampling.LANCZOS)
save_image = ImageTk.PhotoImage(save_resized)
save_button = Button(window, image=save_image, border=0, bg="black", command=save_game)
save = canvas_main.create_window(window_width / 2, window_height / 2 - 50, window=save_button)
canvas_main.itemconfig(save, state="hidden")
save_coords = canvas_main.coords(save)

""" load button """
load_org = Image.open("images/load.png")
load_resized = load_org.resize((204, 80), Image.Resampling.LANCZOS)
load_image = ImageTk.PhotoImage(load_resized)
load_button = Button(window, image=load_image, border=0, bg="black", command=load_game)
load = canvas_main.create_window(window_width / 2, window_height / 2 - 100, window=load_button)
canvas_main.itemconfig(load, state="hidden")
load_coords = canvas_main.coords(load)

""" cheat button """
cheat_org = Image.open("images/cheat.png")
cheat_resized = cheat_org.resize((204, 75), Image.Resampling.LANCZOS)
cheat_image = ImageTk.PhotoImage(cheat_resized)
cheat_button = Button(window, image=cheat_image, border=0, bg="black", command=cheat_codes)
cheats = canvas_main.create_window(window_width / 2, window_height / 2 - 50, window=cheat_button)
canvas_main.itemconfig(cheats, state="hidden")
cheat_coords = canvas_main.coords(cheats)

""" help button """
help_org = Image.open("images/help.png")
help_resized = help_org.resize((204, 80), Image.Resampling.LANCZOS)
help_image = ImageTk.PhotoImage(help_resized)
help_button = Button(window, image=help_image, border=0, bg="black", command=help_player)
helps = canvas_main.create_window(window_width / 2, window_height / 2 + 50, window=help_button)
canvas_main.itemconfig(helps, state="hidden")
help_coords = canvas_main.coords(helps)

""" back button """
back_org = Image.open("images/back.png")
back_resized = back_org.resize((204, 75), Image.Resampling.LANCZOS)
back_image = ImageTk.PhotoImage(back_resized)
back_button = Button(window, image=back_image, border=0, bg="black", command=back_clear)
backs = canvas_main.create_window(window_width / 2, window_height - window_height / 7, window=back_button)
canvas_main.itemconfig(backs, state="hidden")

""" back1 button """
back1_org = Image.open("images/back.png")
back1_resized = back1_org.resize((204, 75), Image.Resampling.LANCZOS)
back1_image = ImageTk.PhotoImage(back1_resized)
back1_button = Button(window, image=back1_image, border=0, bg="black", command=back_clear_to_options)
back1s = canvas_main.create_window(window_width / 2, window_height - window_height / 7, window=back1_button)
canvas_main.itemconfig(back1s, state="hidden")

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
