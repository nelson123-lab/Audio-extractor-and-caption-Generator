import av

# Get the path to the video file
video_file = "Onam Playlist _ Nonstop Onapattukal _Evergreen Onam songs _ SanreeZone _.mp4"

# Open the video file
container = av.open(video_file)

# Find the audio stream
audio_stream = next(s for s in container.streams if s.type == 'audio')

# Extract the audio frames
audio_frames = []
for frame in container.decode(audio_stream):
    audio_frames.append(frame)

# Save the audio frames to a file
audio_file = "Nonstop Onapattukal .wav"
with av.open(audio_file, 'w') as output:
    output.metadata['title'] = 'Nonstop Onapattukal'
    output.metadata['artist'] = 'SanreeZone'
    output.metadata['album'] = 'Onam Playlist'
    output.metadata['year'] = '2023'
    output.metadata['genre'] = 'Onam songs'
    for frame in audio_frames:
        output.mux(frame)

# Close the container
container.close()
