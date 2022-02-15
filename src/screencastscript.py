"""Implements the central object of ScreencastScript."""
import os
import subprocess
import time


class ScreencastScript:
    """Base class for everything.

    This program:
      - Sends commands to other programs (kitty, xdotool)
      - Takes screenshots (scrot)
      - Converts the png files to video (ffmpeg)

    The png files are stored by default in the folder: `img/`.

    At the moment it can only send commands in sequence and is not aware of when the command result
    is displayed on the screen.

    Currently the length of the video is set indirectly using commands that takes screenshots:
    each screenshot is a fraction of a second.

    Examples:
    --------
    # Basic example
    screencast = ScreencastScript()

    # send i3wm commands
    screencast.i3wm_send_command("ws_2")
   
    # Sending commands can be paused 
    screencast.sleep(2)

    # Take screenshots of the screen
    screencast.take_screenshots(8)

    # This will take the png files from folder `img/` to create a video  
    make_video()
    """
    def __init__(self):
        self.prefix = "xdotool"
        self.enter_ret = "Ϟ"  # greek letter koppa
        self.i3wm_actions = {
            "focus_up": [self.prefix, "key", "Alt_L+Up"],
            "focus_right": [self.prefix, "key", "Alt_L+Right"],
            "focus_left": [self.prefix, "key", "Alt_L+Left"],
            "focus_down": [self.prefix, "key", "Alt_L+Down"],
            "zoom_in": [self.prefix, "key", "Control_L+plus"],
            "zoom_out": [self.prefix, "key", "Control_L+underscore"],
            "toggle_fullscreen": [self.prefix, "key", "Alt_L+f"],
            "ws_1": [self.prefix, "key", "Alt_L+1"],
            "ws_2": [self.prefix, "key", "Alt_L+2"],
        }

        self.vim_actions = {
            "insert": [self.prefix, "key", "Escape", "i"],
            "up": [self.prefix, "key", "Escape", "k"],
            "down": [self.prefix, "key", "Escape", "j"],
            "left": [self.prefix, "key", "Escape", "h"],
            "right": [self.prefix, "key", "Escape", "l"],
            "scroll_up": [self.prefix, "key", "Control_L+b"],
            "scroll_down": [self.prefix, "key", "Control_L+f"],
            "vim_split_window_v":
            [self.prefix, "key", "Escape", "Control_L+w", "v"],
            "vim_switch_window":
            [self.prefix, "key", "Escape", "Control_L+w", "w"],
            "vim_close_window":
            [self.prefix, "key", "Escape", "Control_L+w", "c"],
            "vim_save": [self.prefix, "key", "Escape", "Control_L+s"],
            "vim_exit": [self.prefix, "key", "Escape", "colon", "q", "Return"],
        }

        self.nano_actions = {
            "exit": [self.prefix, "key", "Control_L+x"],
            "exit_confirm": [self.prefix, "key", "Control_L+x", "y", "Return"],
        }

    def send_command_take_screenshots(self, command, before=4, after=4):
        self.take_screenshots(before)
        subprocess.run(command)
        self.take_screenshots(after)

    def send_command(self, command):
        subprocess.run(command)

    def nano_send_command(self, command):
        self.send_command(self.nano_actions[command])

    def vim_send_command(self, command):
        self.send_command(self.vim_actions[command])

    def i3wm_send_command(self, command):
        self.send_command(self.i3wm_actions[command])

    def nano_send_command_take_screenshots(self, command, before=4, after=4):
        self.send_command_take_screenshots(self.nano_actions[command], before,
                                           after)

    def vim_send_command_take_screenshots(self, command, before=4, after=4):
        self.send_command_take_screenshots(self.vim_actions[command],
                                           before=4,
                                           after=4)

    def i3wm_send_command_take_screenshots(self, command, before=4, after=4):
        self.send_command_take_screenshots(self.i3wm_actions[command], before,
                                           after)

    def vim_go_to_line(self, n):
        line_n = list(n)
        prefix_key_line_n_go = [self.prefix, "key"] + line_n + ["G"]
        self.send_command([self.prefix, "key", "Escape"])
        self.sleep(1)
        self.send_command(prefix_key_line_n_go)
        self.sleep(1)
        self.send_command([self.prefix, "key", "z", "t"])

    def vim_go_to_line_take_screenshots(self, n, before=4, after=4, path=None):
        line_n = list(n)
        prefix_key_line_n_go = [self.prefix, "key"] + line_n + ["G"]
        self.send_command_take_screenshots([self.prefix, "key", "Escape"],
                                           before,
                                           after,
                                           path=None)
        self.sleep(0.2)
        self.send_command_take_screenshots(prefix_key_line_n_go,
                                           before,
                                           after,
                                           path=None)
        self.sleep(0.2)
        self.send_command_take_screenshots([self.prefix, "key", "z", "t"],
                                           before,
                                           after,
                                           path=None)

    def i3wm_launch(self, program):
        if (program == "gvim"):
            self.send_command([self.prefix, "key", "Super_L+g"])
        elif (program == "vim"):
            self.send_command([self.prefix, "key", "Alt_L+Return"])
            self.sleep(5)
            self.send_command([self.prefix, "key", "v", "i", "m", "Return"])

        elif (program == "kitty"):
            self.send_command([self.prefix, "key", "Alt_L+Return"])

        elif (program == "xonsh"):
            self.send_command([self.prefix, "key", "Alt_L+Return"])
            self.sleep(5)
            self.send_command([
                self.prefix, "key", "x", "o", "n", "s", "h", "space", "minus",
                "minus", "r", "c", "space", "period", "r", "c", "minus", "s",
                "c", "Return"
            ])

    def kitty_launch(self, program, file_name=None):
        if (file_name is not None):
            self.send_command([
                "kitty", "@", "launch", "--type=os-window", program, file_name
            ])
        else:
            self.send_command(
                ["kitty", "@", "launch", "--type=os-window", program])

    def sleep(self, time_to_sleep=0):
        time.sleep(time_to_sleep)

    def __take_png(self, path=None, counter=None, quality="75"):
        if (isinstance(path, str) and isinstance(counter, int)):
            self.send_command([
                "scrot", f'{path}{str(counter)}.png', "--quality", f'{quality}'
            ])
        else:
            print("__take_png, replace this with a better error handler")

    def text_command(self, char):
        if (char == " "):
            return [self.prefix, "key", "space"]

        elif (char == "←"):
            return [self.prefix, "key", "BackSpace"]

        elif (char == "%"):
            return [self.prefix, "key", "percent"]

        elif (char == "*"):
            return [self.prefix, "key", "asterisk"]

        elif (char == "-"):
            return [self.prefix, "key", "minus"]

        elif (char == "+"):
            return [self.prefix, "key", "plus"]

        elif (char == "<"):
            return [self.prefix, "key", "less"]

        elif (char == ">"):
            return [self.prefix, "key", "greater"]

        elif (char == "_"):
            return [self.prefix, "key", "underscore"]

        elif (char == "/"):
            return [self.prefix, "key", "slash"]

        elif (char == "\\"):
            return [self.prefix, "key", "backslash"]

        elif (char == "="):
            return [self.prefix, "key", "equal"]

        elif (char == "."):
            return [self.prefix, "key", "period"]

        elif (char == ","):
            return [self.prefix, "key", "comma"]

        elif (char == ":"):
            return [self.prefix, "key", "colon"]

        elif (char == "'"):
            return [self.prefix, "key", "apostrophe"]

        elif (char == '"'):
            return [self.prefix, "key", "quotedbl"]

        elif (char == ";"):
            return [self.prefix, "key", "semicolon"]

        elif (char == "("):
            return [self.prefix, "key", "parenleft"]

        elif (char == ")"):
            return [self.prefix, "key", "parenright"]

        elif (char == "["):
            return [self.prefix, "key", "bracketleft"]

        elif (char == "]"):
            return [self.prefix, "key", "bracketright"]

        elif (char == "{"):
            return [self.prefix, "key", "braceleft"]

        elif (char == "}"):
            return [self.prefix, "key", "braceright"]

        elif (char == "#"):
            return [self.prefix, "key", "numbersign"]

        elif (char == "Ϟ"):
            return [self.prefix, "key", "Return"]

        elif (char == "\n"):
            return [self.prefix, "key", "Return"]

        elif (char == "Ϡ"):
            return [self.prefix, "key", "Control_L+s"]

        else:
            return [self.prefix, "key", char]

    def send_input(self, text, sleep=0):
        for char in text:
            self.send_command(self.text_command(char))
            self.sleep(sleep)

    def send_input_take_screenshots(self,
                                    text,
                                    path="./img/",
                                    quality="75",
                                    sleep=0.2):

        # counter: number of png files on {path}
        counter = len(os.listdir(path))
        for char in text:
            counter += 1
            self.send_command(self.text_command(char))
            # sleep: when completedProcess is returned, there is nothing in the screen
            self.sleep(sleep)
            self.__take_png(path, counter, quality)

    def take_screenshots(self, n=1, path="./img/", quality="75", sleep=0):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        counter = len(os.listdir(path))
        for x in range(n):
            counter += 1
            self.__take_png(path, counter, quality)
            self.sleep(sleep)

    def make_video_chunk(self,
                         path=None,
                         texts=None,
                         commands=None,
                         quality="75",
                         frame_duration=0.2,
                         video_name="video",
                         video_ext=".mp4"):
        """
        texts:    [{
                    "text_code": str,
                    "sleep": n,
                  }]
    
        commands: [{
                     "func": function_name,
                     "params": [1..n],
                     "sleep": n,
                     "screenshot_n": n  
                     }]
    
        texts or commands for one video
        """

        if (isinstance(path, str)):
            os.makedirs(os.path.dirname(path), exist_ok=True)
        else:
            print("make_video_chunk, replace this with a better error handler")

        # send input an take screenshot
        if (isinstance(texts, list) and len(texts) > 0):
            text_screenshot_counter = len(os.listdir(path))
            for text in texts:
                sleep_text = text["sleep"] if "sleep" in text else 0
                for char in text["text_code"]:
                    text_screenshot_counter += 1
                    self.send_command(self.text_command(char))
                    self.__take_png(path, text_screenshot_counter, quality)
                    self.sleep(sleep_text)
        else:
            print("make_video_chunk, replace this with a better error handler")

        # commands and  take screeenshots
        if (isinstance(commands, list) and len(commands) > 0):
            screenshot_counter = len(os.listdir(path))
            for command in commands:
                sleep_command = command["sleep"]
                screenshot_n = command[
                    "screenshot_n"] if "screenshot_n" in command else 1
                command["func"](*command["params"])
                self.sleep(sleep_command)

                for x in range(screenshot_n):
                    screenshot_counter += 1
                    self.__take_png(path, screenshot_counter, quality)
                    self.sleep(sleep_command)
        else:
            print("make_video_chunk, replace this with a better error handler")

        self.make_video(self, path, frame_duration, video_name, video_ext)

    def make_video_with_audio(self,
                              SOURCE_DIR="./img/",
                              frame_duration=0.25,
                              video_name="video",
                              video_ext=".mp4",
                              audio_file=None,
                              audio_volume="0.20"):

        if (isinstance(audio_file, str)):
            self.make_video(SOURCE_DIR, frame_duration, video_name, video_ext,
                            audio_file, audio_volume)

    def make_video(self,
                   SOURCE_DIR="./img/",
                   frame_duration=0.25,
                   video_name="video",
                   video_ext=".mp4",
                   audio_file=None,
                   audio_volume="1"):

        os.makedirs(os.path.dirname(SOURCE_DIR), exist_ok=True)

        video = [
            "ffmpeg", "-safe", "0", "-f", "concat", "-i", f"{video_name}.txt",
            "-framerate", "25", "-vcodec", "libx264", "-crf", "18", "-pix_fmt",
            "yuv420p", f"{video_name}{video_ext}"
        ]

        video_with_audio = [
            "ffmpeg", "-safe", "0", "-f", "concat", "-i", f"{video_name}.txt",
            "-i", audio_file, "-filter:a", f"volume={audio_volume}",
            "-framerate", "25", "-vcodec", "libx264", "-crf", "18", "-pix_fmt",
            "yuv420p", f"{video_name}{video_ext}"
        ]

        ffmpeg_command = video_with_audio if isinstance(audio_file,
                                                        str) else video

        png_list = os.listdir(SOURCE_DIR)
        png_list = [x.replace(".png", "") for x in os.listdir(SOURCE_DIR)]

        png_list.sort(key=int)

        png_list = [x + ".png" for x in png_list]

        with open(f'{video_name}.txt', "w") as file:
            for image in png_list:
                file.write(
                    f"file '{SOURCE_DIR}{image}'  \nduration {frame_duration}\n"
                )
        """
         https://trac.ffmpeg.org/wiki/Slideshow
         Due to a quirk,
         the last image has to be specified twice - the 2nd time without any duration directive
        """
        with open(f'{video_name}.txt', "a") as file:
            file.write(f"file '{SOURCE_DIR}{png_list[len(png_list) - 1]}'\n")
        self.send_command(ffmpeg_command)
