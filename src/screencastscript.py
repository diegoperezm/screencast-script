import os
import subprocess
import time


class ScreencastScript:
    def __init__(self):
        self.prefix = "xdotool"
        self.enter_ret = "Ϟ"  # greek letter koppa

    def i3wm_focus_left(self):
        self.send_command([self.prefix, "key", "Alt_L+Left"])

    def i3wm_zoom_in(self):
        self.send_command([self.prefix, "key", "Control_L+plus"])

    def i3wm_zoom_out(self):
        self.send_command([self.prefix, "key", "Control_L+underscore"])

    def i3wm_focus_right(self):
        self.send_command([self.prefix, "key", "Alt_L+Right"])

    def i3wm_focus_up(self):
        self.send_command([self.prefix, "key", "Alt_L+Up"])

    def i3wm_focus_down(self):
        self.send_command([self.prefix, "key", "Alt_L+Down"])

    def i3wm_toggle_fullscreen(self):
        self.send_command([self.prefix, "key", "Alt_L+f"])

    def i3wm_ws_1(self):
        self.send_command([self.prefix, "key", "Alt_L+1"])

    def i3wm_ws_2(self):
        self.send_command([self.prefix, "key", "Alt_L+2"])

    def vim_insert(self):
        self.send_command([self.prefix, "key", "Escape", "i"])

    def vim_up(self):
        self.send_command([self.prefix, "key", "Escape", "k"])

    def vim_down(self):
        self.send_command([self.prefix, "key", "Escape", "j"])

    def vim_left(self):
        self.send_command([self.prefix, "key", "Escape", "h"])

    def vim_right(self):
        self.send_command([self.prefix, "key", "Escape", "l"])

    def vim_scroll_up(self):
        self.send_command([self.prefix, "key", "Control_L+b"])

    def vim_scroll_down(self):
        self.send_command([self.prefix, "key", "Control_L+f"])

    def vim_go_to_line(self, n):
        line_n = list(n)
        prefix_key_line_n_go = [self.prefix, "key"] + line_n + ["G"]
        self.send_command([self.prefix, "key", "Escape"])
        time.sleep(1)
        self.send_command(prefix_key_line_n_go)
        time.sleep(1)
        self.send_command([self.prefix, "key", "z", "t"])

    def vim_split_window_v(self):
        self.send_command([self.prefix, "key", "Escape", "Control_L+w", "v"])

    def vim_switch_window(self):
        self.send_command([self.prefix, "key", "Escape", "Control_L+w", "w"])

    def vim_close_window(self):
        self.send_command([self.prefix, "key", "Escape", "Control_L+w", "c"])

    def vim_save(self):
        self.send_command([self.prefix, "key", "Escape", "Control_L+s"])

    def vim_exit(self):
        self.send_command(
            [self.prefix, "key", "Escape", "colon", "q", "Return"])

    def nano_exit(self):
        self.send_command([self.prefix, "key", "Control_L+x"])

    def nano_exit_confirm(self):
        self.send_command([self.prefix, "key", "Control_L+x", "y", "Return"])

    def i3wm_zoom_in_take_screenshots(self, before=4, after=4):
        self.send_command_take_screenshots(
            [self.prefix, "key", "Control_L+plus"], before, after)

    def i3wm_zoom_out_take_screenshots(self, before=4, after=4):
        self.send_command_take_screenshots(
            [self.prefix, "key", "Control_L+underscore"], before, after)

    def i3wm_focus_left_take_screenshots(self, before=4, after=4):
        self.send_command_take_screenshots([self.prefix, "key", "Alt_L+Left"],
                                           before, after)

    def i3wm_focus_right_take_screenshots(self, before=4, after=4):
        self.send_command_take_screenshots([self.prefix, "key", "Alt_L+Right"],
                                           before, after)

    def i3wm_focus_up_take_screenshots(self, before=4, after=4):
        self.send_command_take_screenshots([self.prefix, "key", "Alt_L+Up"],
                                           before, after)

    def i3wm_focus_down_take_screenshots(self, before=4, after=4):
        self.send_command_take_screenshots([self.prefix, "key", "Alt_L+Down"],
                                           before, after)

    def i3wm_toggle_fullscreen_take_screenshots(self, before=4, after=4):
        self.send_command_take_screenshots([self.prefix, "key", "Alt_L+f"],
                                           before, after)

    def i3wm_ws_1_take_screenshots(self, before=4, after=4):
        self.send_command_take_screenshots([self.prefix, "key", "Alt_L+1"],
                                           before, after)

    def i3wm_ws_2_take_screenshots(self, before=4, after=4):
        self.send_command_take_screenshots([self.prefix, "key", "Alt_L+2"],
                                           before, after)

    def vim_insert_take_screenshots(self, before=4, after=4):
        self.send_command_take_screenshots([self.prefix, "key", "Escape", "i"],
                                           before, after)

    def vim_up_take_screenshots(self, before=4, after=4):
        self.send_command_take_screenshots([self.prefix, "key", "Escape", "k"],
                                           before, after)

    def vim_down_take_screenshots(self, before=4, after=4):
        self.send_command_take_screenshots([self.prefix, "key", "Escape", "j"],
                                           before, after)

    def vim_left_take_screenshots(self, before=4, after=4):
        self.send_command_take_screenshots([self.prefix, "key", "Escape", "h"],
                                           before, after)

    def vim_right_take_screenshots(self, before=4, after=4):
        self.send_command_take_screenshots([self.prefix, "key", "Escape", "l"],
                                           before, after)

    def vim_scroll_up_take_screenshots(self, before=4, after=4):
        self.send_command_take_screenshots([self.prefix, "key", "Control_L+b"],
                                           before, after)

    def vim_scroll_down_take_screenshots(self, before=4, after=4):
        self.send_command_take_screenshots([self.prefix, "key", "Control_L+f"],
                                           before, after)

    def vim_go_to_line_take_screenshots(self, n, before=4, after=4):
        line_n = list(n)
        prefix_key_line_n_go = [self.prefix, "key"] + line_n + ["G"]
        self.send_command_take_screenshots([self.prefix, "key", "Escape"],
                                           before, after)
        time.sleep(0.2)
        self.send_command_take_screenshots(prefix_key_line_n_go, before, after)
        time.sleep(0.2)
        self.send_command_take_screenshots([self.prefix, "key", "z", "t"],
                                           before, after)

    def vim_split_window_v_take_screenshots(self, before=4, after=4):
        self.send_command_take_screenshots(
            [self.prefix, "key", "Escape", "Control_L+w", "v"], before, after)

    def vim_switch_window_take_screenshots(self, before=4, after=4):
        self.send_command_take_screenshots(
            [self.prefix, "key", "Escape", "Control_L+w", "w"], before, after)

    def vim_close_window_take_screenshots(self, before=4, after=4):
        self.send_command_take_screenshots(
            [self.prefix, "key", "Escape", "Control_L+w", "c"], before, after)

    def vim_save_take_screenshots(self, before=4, after=4):
        self.send_command_take_screenshots(
            [self.prefix, "key", "Escape", "Control_L+s"], before, after)

    def vim_exit_take_screenshots(self, before=4, after=4):
        self.send_command_take_screenshots(
            [self.prefix, "key", "Escape", "colon", "q", "Return"], before,
            after)

    def nano_exit_take_screenshots(self, before=4, after=4):
        self.send_command_take_screenshots([self.prefix, "key", "Control_L+x"],
                                           before, after)

    def nano_exit_confirm_take_screenshots(self, before=4, after=4):
        self.send_command_take_screenshots(
            [self.prefix, "key", "Control_L+x", "y", "Return"], before, after)

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
            time.sleep(sleep)

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
            time.sleep(sleep)
            self.__take_png(path, counter, quality)

    def take_screenshots(self, n=1, path="./img/", quality="75", sleep=0):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        counter = len(os.listdir(path))
        for x in range(n):
            counter += 1
            self.__take_png(path, counter, quality)
            time.sleep(sleep)

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
                    time.sleep(sleep_text)
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
                time.sleep(sleep_command)

                for x in range(screenshot_n):
                    screenshot_counter += 1
                    self.__take_png(path, screenshot_counter, quality)
                    time.sleep(sleep_command)
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

    def i3wm_launch(self, program):
        if (program == "gvim"):
            self.send_command([self.prefix, "key", "Super_L+g"])

        elif (program == "vim"):
            self.send_command([self.prefix, "key", "Alt_L+Return"])
            time.sleep(5)
            self.send_command([self.prefix, "key", "v", "i", "m", "Return"])

        elif (program == "kitty"):
            self.send_command([self.prefix, "key", "Alt_L+Return"])

        elif (program == "xonsh"):
            self.send_command([self.prefix, "key", "Alt_L+Return"])
            time.sleep(5)
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

    def send_command_take_screenshots(self, command, before=4, after=4):
        self.take_screenshots(before)
        subprocess.run(command)
        self.take_screenshots(after)

    def send_command(self, command):
        subprocess.run(command)
