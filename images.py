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
