import sys
# for development
sys.path.append('../../src')

from screencastscript import ScreencastScript  # noqa: E402

screencast = ScreencastScript()
screencast.sleep(1)

screencast.i3wm_focus_left()
screencast.sleep(1)

screencast.i3wm_zoom_in()
screencast.sleep(1)

screencast.i3wm_zoom_out()
screencast.sleep(1)

screencast.i3wm_focus_right()
screencast.sleep(1)

screencast.i3wm_focus_up()
screencast.sleep(1)

screencast.i3wm_focus_down()
screencast.sleep(1)

screencast.i3wm_toggle_fullscreen()
screencast.sleep(1)

screencast.i3wm_ws_2()
screencast.sleep(1)

screencast.i3wm_ws_1()
screencast.sleep(1)
