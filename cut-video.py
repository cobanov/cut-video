from moviepy.editor import *

vcodec = "libx264"
videoquality = "24"
# slow, ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow
compression = "ultrafast"

path = "/Users/mertcobanoglu/Youtube-Contents/Final-Video/colab_son.mov"

# Load myHolidays.mp4 and select the subclip 00:00:50 - 00:00:60
clip = VideoFileClip(path).subclip(0, 10)

# Reduce the audio volume (volume x 0.8)
#clip = clip.volumex(1)

# Generate a text clip. You can customize the font, color, etc.
#txt_clip = TextClip("Eğitimler Youtube: Mert Cobanov", fontsize=70, color='white', font="Helvetica")


# Say that you want it to appear 10s at the center of the screen
#txt_clip = txt_clip.set_pos('bottom').set_duration(5)

# Overlay the text clip on the first video clip
#video = CompositeVideoClip([clip, txt_clip])
video = CompositeVideoClip([clip])

# Write the result to a file (many options available !)
video.write_videofile("output.mp4", codec=vcodec,
                               preset=compression,
                               ffmpeg_params=["-crf",videoquality])

