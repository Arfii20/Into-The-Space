# Coursework 2 of COMP16321

"""
*** The screen resolution is 1440x900

* This is a classic asteroid game where the player needs to avoid hitting the asteroids to survive.
* The difficulty increases at certain scores.
* The speed of the asteroids will increase making the game harder and harder at each level.
"""

# game_icon.ico source: https://www.freeiconspng.com/img/17270
# spaceship_image.png source: https://www.pngkey.com/detail/u2q8a9t4r5y3a9r5_spaceship-png-file-spaceship-png/
# asteroid_1.png source: https://www.pngmart.com/image/50759
# asteroid_2.png source: https://pngimg.com/image/105528
# asteroid_3.png source: https://pngimg.com/image/105498
# asteroid_4.png source: https://pngimg.com/image/105494
# background.jpg source: https://www.pexels.com/photo/starry-sky-998641/
# background.jpg source: Photo by Aleksandar Pasaric: https://www.pexels.com/photo/dark-starry-sky-1694000/


from tkinter import *
from tkinter.font import Font
from PIL import Image, ImageTk


# Configure main window
def configure_root():
    root.title("Asteroid Game")
    root.iconbitmap("images/game_icon.ico")
    root.configure()

    # Disabled resizing of the window
    root.resizable(False, False)

    """ Fixing geometry so that the window opens at the center """
    # Width and height of the window
    width = window_width
    height = window_height

    # Screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Change of coordinates
    x = int(screen_width / 2 - width / 2)
    y = int(screen_height / 2 - height / 2 - 20)

    # screen position
    root.geometry(f"{width}x{height}+{x}+{y}")


# Creating keybindings to move the spaceship
def move_spaceship_left(e):
    x = -10
    y = 0
    canvas_main.move(spaceship, x, y)


def move_spaceship_right(e):
    x = 10
    y = 0
    canvas_main.move(spaceship, x, y)


def move_spaceship_up(e):
    x = 0
    y = -10
    canvas_main.move(spaceship, x, y)


def move_spaceship_down(e):
    x = 0
    y = 10
    canvas_main.move(spaceship, x, y)


# Creating main game function
def main_game():
    """Adding Background to the pain game"""
    # Open background image
    global background_image
    background_image = ImageTk.PhotoImage(Image.open("images/background.jpg"))

    # Creating a Canvas
    global canvas_main
    canvas_main = Canvas(root, width=window_width, height=window_height)
    canvas_main.pack(fill="both", expand=True)

    # Add background to canvas
    canvas_main.create_image(0, 0, image=background_image, anchor=NW)

    # Resize spaceship
    global spaceship_image
    spaceship_org = Image.open("images/spaceship_image.png")
    spaceship_resized = spaceship_org.resize((80, 80), Image.Resampling.LANCZOS)
    spaceship_image = ImageTk.PhotoImage(spaceship_resized)

    # Add spaceship to canvas
    global spaceship
    x = 690
    y = 750
    spaceship = canvas_main.create_image(x, y, image=spaceship_image, anchor=NW)


    # Keybindings
    root.bind("<Left>", move_spaceship_left)
    root.bind("<Right>", move_spaceship_right)
    root.bind("<Up>", move_spaceship_up)
    root.bind("<Down>", move_spaceship_down)

    Label1 = Label(canvas_main, text="Score: 0", font=custom_font, bg="black", fg="white")
    Label1.place(relx=0.79, rely=0.05)

root = Tk()

"""Defining variables"""
# Width and height of the window
window_width = 1440
window_height = 900

# custom font
custom_font = Font(
    family="MV Boli",
    size=35,
)

configure_root()
main_game()

root.mainloop()
