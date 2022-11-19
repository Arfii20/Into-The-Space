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
cheat_resized = cheat_org.resize((204, 80), Image.Resampling.LANCZOS)
cheat_image = ImageTk.PhotoImage(cheat_resized)
cheat_button = Button(window, image=cheat_image, border=0, bg="black", command=cheat_game)
cheat = canvas_main.create_window(window_width / 2, window_height / 2 - 100, window=cheat_button)
canvas_main.itemconfig(cheat, state="hidden")
cheat_coords = canvas_main.coords(cheat)

""" back button """
back_org = Image.open("images/back.png")
back_resized = back_org.resize((204, 80), Image.Resampling.LANCZOS)
back_image = ImageTk.PhotoImage(back_resized)


""" Spaceship """
spaceship_org = Image.open("images/spaceship_image.png")
spaceship_resized = spaceship_org.resize((100, 100), Image.Resampling.LANCZOS)
spaceship_image = ImageTk.PhotoImage(spaceship_resized)
spaceship = canvas_main.create_image(window_width / 2 - 40,
                                     window_height - window_height / 6,
                                     image=spaceship_image, anchor="nw")
canvas_main.itemconfig(spaceship, state="hidden")