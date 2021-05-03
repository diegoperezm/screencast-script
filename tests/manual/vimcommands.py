import sys
# for development
sys.path.append('../../src')

from screencastscript import ScreencastScript  # noqa: E402

screencast = ScreencastScript()
screencast.sleep(3)

screencast.vim_up()
screencast.sleep(1)

screencast.vim_down()
screencast.sleep(1)

screencast.vim_left()
screencast.sleep(1)

screencast.vim_right()
screencast.sleep(1)

screencast.vim_scroll_up()
screencast.sleep(1)

screencast.vim_scroll_down()
screencast.sleep(1)

screencast.vim_split_window_v()
screencast.sleep(1)

screencast.vim_switch_window()
screencast.sleep(1)

screencast.vim_close_window()
screencast.sleep(1)

screencast.vim_go_to_line("44")
screencast.sleep(1)

screencast.vim_insert()
screencast.sleep(1)

msg = """

"""
