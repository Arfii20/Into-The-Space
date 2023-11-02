"""
The next sections are about loading, resizing and storing images to variables.
Using the images, buttons are created and the state is set to hidden to use later.
Position of the buttons are fixed using the coords function.
"""


from PIL import Image


"Use default button."
use_default_org = Image.open("images/use_default.png")
use_default_resized = use_default_org.resize((400, 75))

"Change name button."
change_name_org = Image.open("images/change_name.png")
change_name_resized = change_name_org.resize((400, 75))

"Done button."
done_org = Image.open("images/done.png")
done_resized = done_org.resize((200, 75))

"Start button."
start_org = Image.open("images/start.png")
start_resized = start_org.resize((200, 75))

"Resume button."
resume_org = Image.open("images/resume.png")
resume_resized = resume_org.resize((244, 80))

"Restart button."
restart_org = Image.open("images/restart.png")
restart_resized = restart_org.resize((244, 80))

"Save button."
save_org = Image.open("images/save.png")
save_resized = save_org.resize((204, 80))

"Load button."
load_org = Image.open("images/load.png")
load_resized = load_org.resize((204, 80))

"Leaderboard button."
leaderboard_org = Image.open("images/leaderboard.png")
leaderboard_resized = leaderboard_org.resize((474, 80))

"Options button."
options_org = Image.open("images/options.png")
options_resized = options_org.resize((240, 75))

"Cheat button."
cheat_org = Image.open("images/cheat.png")
cheat_resized = cheat_org.resize((204, 75))

"Key_binds button."
key_binds_org = Image.open("images/key_binds.png")
key_binds_resized = key_binds_org.resize((354, 80))

"Arrows button."
arrows_org = Image.open("images/arrows.png")
arrows_resized = arrows_org.resize((334, 90))

"Wasd button."
wasd_org = Image.open("images/wasd.png")
wasd_resized = wasd_org.resize((254, 90))

"Help button."
help_org = Image.open("images/help.png")
help_resized = help_org.resize((174, 80))

"Back button."
back_org = Image.open("images/Back.png")
back_resized = back_org.resize((204, 75))

"Back button to options."
back1_org = Image.open("images/back.png")
back1_resized = back1_org.resize((204, 75))

"Exit button."
exit_org = Image.open("images/exit.png")
exit_resized = exit_org.resize((200, 70))

"Spaceship."
spaceship_org = Image.open("images/spaceship_image.png")
spaceship_resized = spaceship_org.resize((100, 100))