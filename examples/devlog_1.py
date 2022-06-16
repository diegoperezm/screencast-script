import sys
# for development
sys.path.append('./src')
sys.path.append('../src')

from screencastscript import ScreencastScript  # noqa: E402
screencast = ScreencastScript()

screencast.make_video(frame_duration=0.05)

# If you want to use this, you need an audio file (in the folder)
# screencast.make_video_with_audio(
#     audio_file="./audio.mp3")
