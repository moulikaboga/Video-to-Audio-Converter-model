# converter.py
import os
from moviepy.editor import VideoFileClip

def video_to_audio(video_filename, output_format="mp3"):
    """Convert video file to audio file."""
    # Load video
    video_clip = VideoFileClip(video_filename)

    # Extract audio
    audio = video_clip.audio

    # Define output filename
    audio_output_filename = os.path.splitext(video_filename)[0] + f".{output_format}"

    # Write audio to file
    audio.write_audiofile(audio_output_filename)

    return audio_output_filename

if __name__ == "__main__":
    # Example usage
    video_file = input("Enter the video filename (with extension): ")
    output = video_to_audio(video_file)
    print(f"✅ Audio saved as: {output}")
