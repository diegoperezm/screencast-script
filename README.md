# screencast-script 
>  

> 🚧 Work in progress 🚧

A simple script that:

 - Sends commands to other programs (kitty, xdotool)
 - Takes screenshots (scrot)
 - Converts the png files to video (ffmpeg)

[Video](https://youtu.be/dWMk2oIwnPg)


## Basic example

The png files are stored by default in the folder: `img/`.

At the moment it can only send commands in sequence and is not aware of when the command result is displayed on the screen.

Currently the length of the video is set indirectly using commands that takes screenshots: each screenshot is a fraction of a second.

```python

screencast = ScreencastScript()

# send i3wm commands
screencast.i3wm_ws_2()

# Sending commands can be paused 
screencast.sleep(2)

# Take screenshots of the screen
screencast.take_screenshots(8)

# This will take the png files from folder `img/` to create a video  
make_video()
``` 

## Installing / Getting started

Tested using:

- vim 
- i3wm
- kitty 0.20.1 [with allow remote control enabled](https://sw.kovidgoyal.net/kitty/remote-control.html?highlight=allow)
- [scrot 0.8](https://en.wikipedia.org/wiki/Scrot)
- xdotool 3.20160805.1
- ffmpeg 4.3.2.2ubuntu0~18.04


## Licensing

"The code in this project is licensed under MIT license."
