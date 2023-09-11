import ffmpeg

# Get the path to the video file
video_file = "video.mp4"

# Create an ffmpeg object
ffmpeg_object = ffmpeg.FFmpeg()

# Extract the audio from the video file
audio_file = ffmpeg_object.input(video_file).output("audio.wav").run()

# Save the audio file
with open("audio.wav", "wb") as f:
    f.write(audio_file)
