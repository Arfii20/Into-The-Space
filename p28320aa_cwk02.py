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
# background_image.jpg source: https://phys.org/news/2022-08-ai-space-anomalies.html


from tkinter import *


def configure_root():
    root.title("Asteroid Game")
    root.iconbitmap("images/game_icon.ico")
    root.configure()

    """ Fixing geometry so that the window opens at the center """
    # Width and height of the window
    width = 1440
    height = 900

    # Screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Change of coordinates
    x = int(screen_width / 2 - width / 2)
    y = int(screen_height / 2 - height / 2)

    # screen position
    root.geometry(f"{width}x{height}+{x}+{y}")

root = Tk()
configure_root()




root.mainloop()