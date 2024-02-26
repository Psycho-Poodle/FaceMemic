# ElevenLab
#!pip install elevenlabs -U
from Translate import translated_text
import elevenlabs


from elevenlabs import set_api_key,clone,generate,play

set_api_key("1656cb2a5373f912ad1782b5a4ce7113")


voice = clone(
   name = "My Cloned Voice",
   files = ['Videos/extracted_audio.wav']
)


audio = generate(translated_text, voice=voice)


play(audio, notebook=True)



#Save audio
# Assuming "audio" is a byte object containing the audio data

output_path = "Videos/clone_vic.wav"

with open(output_path, "wb") as f:
    f.write(audio)
