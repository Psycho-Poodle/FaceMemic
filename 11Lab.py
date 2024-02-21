# ElevenLab
!pip install elevenlabs -U
import elevenlabs


from elevenlabs import set_api_key,clone,generate,play

set_api_key("bdb613a1499579e87e1df106784b6ef0")


voice = clone(
   name = "My Cloned Voice",
   files = ['/kaggle/working/clone_vic.wav']
)


audio = generate(translated_text, voice=voice)


play(audio, notebook=True)



#Save audio
# Assuming "audio" is a byte object containing the audio data

output_path = "Results/clone_vic.wav"

with open(output_path, "wb") as f:
    f.write(audio)
