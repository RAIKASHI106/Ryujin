import os
import subprocess

# Path to the video you want to convert
INPUT_VIDEO = "Media_Raw\\Evangelion\\NGE - 01.mkv"
# Folder where HLS output will go
OUTPUT_FOLDER = "hls_output"
# FFmpeg executable
FFMPEG = "C:\\ffmeg\\ffmpeg-master-latest-win64-gpl-shared\\bin\\ffmpeg.exe"

# Create output folder if it doesn't exist
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Base HLS parameters
HLS_OPTIONS = [
    "-profile:v", "main",       # H.264 main profile
    "-crf", "20",               # Quality
    "-sc_threshold", "0",       # Scene change threshold
    "-g", "48",                 # GOP size (2s for 24fps)
    "-keyint_min", "48",
    "-hls_time", "4",           # Each segment 4 seconds
    "-hls_playlist_type", "vod" # VOD playlist
]

# Output master playlist and stream info
VIDEO_STREAM = os.path.join(OUTPUT_FOLDER, "video.m3u8")
AUDIO_STREAM = os.path.join(OUTPUT_FOLDER, "audio.m3u8")

# Command for FFmpeg to generate HLS with separate audio/video streams
command = [
    FFMPEG,
    "-i", INPUT_VIDEO,
    "-map", "0:v:0", "-map", "0:a:0?",  # map video and first audio track
    "-c:v", "libx264", "-c:a", "aac",  # encode video/audio
    *HLS_OPTIONS,
    os.path.join(OUTPUT_FOLDER, "master.m3u8")
]

print("Running FFmpeg to generate HLS segments...")
subprocess.run(command, check=True)
print("HLS conversion done. Segments are in:", OUTPUT_FOLDER)
