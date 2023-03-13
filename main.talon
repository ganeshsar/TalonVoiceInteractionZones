
-

settings():
    key_wait = 2.0

scroll up command:
    user.mouse_scroll_up(1)
scroll down command:
    user.mouse_scroll_down(1)

scrolling zone:
    user.add_zone("up", 50, 1920-50, 50, 310, 10, 500, "scroll up command")
    user.add_zone("down", 50, 1920-50, 1080-310, 1080-50, 10, 500, "scroll down command")
    user.enable_zones()

stop zone:
    user.disable_zones()
