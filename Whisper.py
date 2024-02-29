import torch
import os
import librosa
import whisper
from pydub import AudioSegment
# !pip install moviepy
from moviepy.editor import VideoFileClip
from googletrans import Translator
#from gtts import gTTS
from IPython.display import HTML, clear_output
from IPython.display import HTML, Audio
# from google.colab.output import eval_js
from base64 import b64decode
import numpy as np
from scipy.io.wavfile import read as wav_read
import io
import ffmpeg
# from ghc.l_ghc_cf import l_ghc_cf
import soundfile as sf
from IPython.display import Audio
from IPython.core.display import display
import shutil
# from google.colab import drive
# from google.colab import files
from IPython.display import HTML, clear_output
from base64 import b64encode
import moviepy.editor as mp
from IPython.display import HTML
from base64 import b64encode


# Set the device
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load the model
whisper_model = whisper.load_model("large", device=device)





import os
from moviepy.editor import VideoFileClip

def video_to_audio(video_path, destination, final_filename):
    # Check if the file path is valid
    if not os.path.isfile(video_path):
        raise ValueError(f"The provided path '{video_path}' is not a valid file.")

    # Load the video file
    video_clip = VideoFileClip(video_path)

    # Extract audio from the video
    audio_clip = video_clip.audio

    # Set the destination path for the audio file
    path_audio = os.path.join(destination, final_filename + ".wav")

    # Write the audio file
    audio_clip.write_audiofile(path_audio)

    return path_audio

# Example usage
video_path = "Videos/input_vid.mp4"
destination = "Videos/"
final_filename = "extracted_audio"
path_audio = video_to_audio(video_path, destination, final_filename)


audio_file = "Audios/extracted_audio.wav"
result = whisper_model.transcribe(audio_file)
extracted_text = result['text']
print(extracted_text)
