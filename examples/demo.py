import sys
# for development
sys.path.append('./src')
sys.path.append('../src')

from screencastscript import ScreencastScript  # noqa: E402
screencast = ScreencastScript()

##################################
#                                #
#       screencast-script:       #
#            Demo                #
#                                #
##################################

screencast.i3wm_send_command("ws_2")
screencast.sleep(2)

screencast.take_screenshots(2, 8)
screencast.i3wm_send_command("focus_right")

screencast.send_input_take_screenshots(2, """import matplotlib.pyplot as plt
""")

screencast.sleep(4)
screencast.take_screenshots(2, 8)

screencast.send_input_take_screenshots(2, """import numpy as np

""")

screencast.sleep(2)
screencast.take_screenshots(2, 8)

screencast.send_input_take_screenshots(
    2, """x = np.linspace(-np.pi / 2, np.pi / 2, 31)
y = np.cos(x)**3

""")

screencast.sleep(2)
screencast.take_screenshots(2, 8)

screencast.send_input_take_screenshots(
    2, """# 1) remove points where y > 0.7
x2 = x[y <= 0.7]
y2 = y[y <= 0.7]

""")

screencast.sleep(2)
screencast.take_screenshots(2, 8)

screencast.send_input_take_screenshots(
    2, """# 2) mask points where y > 0.7
y3 = np.ma.masked_where(y > 0.7, y)

# 3) set to NaN where y > 0.7
y4 = y.copy()
y4[y3 > 0.7] = np.nan

""")

screencast.sleep(2)
screencast.take_screenshots(2, 8)

screencast.i3wm_send_command("toggle_fullscreen")
screencast.take_screenshots(2, 8)
screencast.sleep(4)

screencast.send_input_take_screenshots(
    2, """plt.plot(x * 0.1, y, 'o-', color='lightgrey', label='No mask')

""")

screencast.sleep(4)
screencast.take_screenshots(2, 8)

screencast.send_input_take_screenshots(2, """plt.show()

""")

screencast.sleep(4)
screencast.take_screenshots(2, 12)

screencast.send_input_take_screenshots(
    2, """plt.plot(x2 * 0.4, y2, 'o-', label='Points removed')

""")

screencast.sleep(4)
screencast.take_screenshots(2, 8)
screencast.send_input_take_screenshots(2, """plt.show()

""")

screencast.sleep(4)
screencast.take_screenshots(2, 12)

screencast.send_input_take_screenshots(
    2, """plt.plot(x * 0.7, y3, 'o-', label='Masked values')

""")

screencast.sleep(4)
screencast.take_screenshots(2, 8)
screencast.send_input("""plt.show()

""")

screencast.sleep(4)
screencast.take_screenshots(2, 12)

screencast.send_input("""plt.plot(x * 1.0, y4, 'o-', label='NaN values')

""")

screencast.sleep(4)
screencast.take_screenshots(2, 12)

screencast.send_input("""plt.legend()

""")

screencast.sleep(4)

screencast.send_input_take_screenshots(
    2, """plt.title('Masked and NaN data')

""")

screencast.sleep(4)
screencast.take_screenshots(2, 4)

screencast.send_input_take_screenshots(2, """plt.show()

""")

screencast.sleep(4)
screencast.take_screenshots(2, 12)

screencast.i3wm_send_command_take_screenshots("toggle_fullscreen")
screencast.take_screenshots(2, 4)

screencast.i3wm_focus_left_take_screenshots(2, )
screencast.take_screenshots(2, 4)
screencast.sleep(2)

screencast.i3wm_send_command_take_screenshots("toggle_fullscreen")
screencast.take_screenshots(2, 4)
screencast.sleep(2)

screencast.i3wm_send_command_take_screenshots(2, "zoom_in")
screencast.sleep(2)
screencast.take_screenshots(2, 8)

screencast.i3wm_send_command_take_screenshots(2, "zoom_in")
screencast.sleep(2)
screencast.take_screenshots(2, 8)

screencast.i3wm_send_command_take_screenshots(2, "zoom_in")
screencast.sleep(2)
screencast.take_screenshots(2, 8)

screencast.vim_send_command_take_screenshots(2, "scroll_down")
screencast.sleep(2)
screencast.take_screenshots(2, 8)

screencast.vim_send_command_take_screenshots(2, "scroll_down")
screencast.sleep(2)
screencast.take_screenshots(2, 8)

screencast.vim_send_command_take_screenshots(2, "scroll_down")
screencast.sleep(2)
screencast.take_screenshots(2, 8)

screencast.vim_send_command_take_screenshots(2, "scroll_down")
screencast.sleep(2)
screencast.take_screenshots(2, 8)

screencast.vim_send_command_take_screenshots(2, "scroll_down")
screencast.sleep(2)
screencast.take_screenshots(2, 8)

screencast.vim_send_command_take_screenshots(2, "scroll_down")
screencast.sleep(2)
screencast.take_screenshots(2, 24)

screencast.make_video()

# If you want to use this, you need an audio file (in the folder)
# screencast.make_video_with_audio(
#     audio_file="./audio.mp3")
