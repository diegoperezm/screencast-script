import os
import time

prefix = "xdotool key"
escape = "Ϟ"  # greek letter koppa
next_line = "#"
insert = "i"

i3wm_focus_left = prefix + " " + "Alt_L+Left"
i3wm_focus_right = prefix + " " + "Alt_L+Right"
i3wm_focus_up = prefix + " " + "Alt_L+Up"
i3wm_focus_down = prefix + " " + "Alt_L+Down"
i3wm_toggle_fullscreen = prefix + " " + "Alt_L+f"

i3wm_ws_1 = prefix + " " + "Alt_L+1"
i3wm_ws_2 = prefix + " " + "Alt_L+2"

vim_insert = prefix + " " + "Escape i"
vim_up = prefix + " " + "Escape k"
vim_down = prefix + " " + "Escape j"
vim_left = prefix + " " + "Escape h"
vim_right = prefix + " " + "Escape l"
vim_scroll_up = prefix + " " + "Control_L+b"
vim_scroll_down = prefix + " " + "Control_L+f"

vim_split_window_v = prefix + " " + "Escape Control_L+w v"
vim_switch_window = prefix + " " + "Escape Control_L+w w"
vim_close_window = prefix + " " + "Escape Control_L+w c"

vim_save = prefix + " " + "Escape Control_L+s"
vim_exit = prefix + " " + "Escape colon q Return"

nano_exit = prefix + " " + "Control_L+x"
nano_exit_confirm = prefix + " " + "Control_L+x y Return"

counter = 0


def take_screenshots(n=1):
    global counter
    for x in range(n):
        counter += 1
        time.sleep(0.5)
        os.system("scrot " + "./img/" + str(counter) + ".png --quality 75")


def send_input_take_screenshots(text, delay_t=0.2):
    for i in text:
        global counter
        counter += 1
        os.system("scrot " + "./img/" + str(counter) + ".png --quality 75")
        time.sleep(delay_t)

        if (i == " "):
            os.system(prefix + " " + "space")

        elif (i == ","):
            os.system(prefix + " " + "comma")

        elif (i == ":"):
            os.system(prefix + " " + "colon")

        elif (i == ";"):
            os.system(prefix + " " + "semicolon")

        elif (i == "("):
            os.system(prefix + " " + "parenleft")

        elif (i == ")"):
            os.system(prefix + " " + "parenright")

        elif (i == "{"):
            os.system(prefix + " " + "braceleft")

        elif (i == "}"):
            os.system(prefix + " " + "braceright")

        elif (i == "#"):
            os.system(prefix + " " + "Return")

        elif (i == "\n"):
            os.system(prefix + " " + "Return")

        elif (i == "Ϟ"):
            os.system(prefix + " " + "Escape")

        elif (i == "Ϡ"):
            os.system(prefix + " " + "Control_L+s")

        else:
            os.system(prefix + " " + i)


def make_video(DURATION=0.25, file_name="video.mp4"):
    SOURCE_DIR = "./img/"
    PNG_LIST = os.listdir(SOURCE_DIR)
    PNG_LIST = [x.replace(".png", "") for x in os.listdir(SOURCE_DIR)]

    PNG_LIST.sort(key=int)

    PNG_LIST = [x + ".png" for x in PNG_LIST]

    with open("input.txt", "w") as file:
        for x in PNG_LIST:
            file.write(f"file '{SOURCE_DIR}{x}'  \nduration {DURATION}\n")
    """
     https://trac.ffmpeg.org/wiki/Slideshow
     Due to a quirk,
     the last image has to be specified twice - the 2nd time without any duration directive
    """
    with open("input.txt", "a") as file:
        file.write(f"file '{SOURCE_DIR}{PNG_LIST[len(PNG_LIST) - 1]}'\n")

    os.system(
        f'ffmpeg -safe 0 -f concat -i input.txt -vf scale="1920x1080" -framerate 25 -vcodec libx264 -crf 28 -pix_fmt yuv420p {file_name}'
    )


def kitty_launch(program, file=""):
    kitty = "/home/erretres/.local/kitty.app/bin/kitty"
    os.system(kitty + " @ launch --type=os-window " + program + " " + file)


def send_command(command):
    os.system(command)


def vim_go_to_line(n):
    c = ''
    for x in n:
        c += x + " "

    os.system(prefix + " " + "Escape")
    time.sleep(1)
    os.system(prefix + " " + c + " " + "G")
    time.sleep(1)
    os.system(prefix + " " + "z t")


#################
#               #
#  SCREENCAST   #
#               #
#################

send_command(i3wm_ws_2)
time.sleep(1)

kitty_launch("vim", "/home/erretres/SCREENCAST/screencast-script.py")
time.sleep(2)
take_screenshots(12)
time.sleep(1)

send_command(vim_split_window_v)
time.sleep(1)
take_screenshots(8)

send_command(vim_switch_window)
time.sleep(1)
take_screenshots(4)

msg = """:e message # Go
Hello,
this script is writing this screencast:
sends commands to other programs#
takes screenshots#
and converts the png files to video using ffmpeg
"""
send_input_take_screenshots(msg)
time.sleep(1)
take_screenshots(16)
time.sleep(1)

send_command(vim_close_window)
time.sleep(2)
take_screenshots(12)

vim_go_to_line("161")
time.sleep(1)
take_screenshots(16)

vim_go_to_line("1")
time.sleep(1)
take_screenshots(16)

vim_go_to_line("37")
time.sleep(1)
take_screenshots(16)

vim_go_to_line("93")
time.sleep(1)
take_screenshots(12)

vim_go_to_line("118")
time.sleep(1)
take_screenshots(16)

vim_go_to_line("139")
time.sleep(1)
take_screenshots(12)

send_command(vim_scroll_down)
time.sleep(1)
take_screenshots(16)

send_command(vim_scroll_down)
time.sleep(1)
take_screenshots(24)

time.sleep(3)

send_command(i3wm_ws_1)
time.sleep(2)

make_video()
