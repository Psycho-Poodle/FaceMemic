
import 11Lab
input_video_path = '/Videos/input_vid.mp4'
input_audio_path = 'Audios/clone_vic.wav'
# %cd Wav2Lip

# Set up paths and variables for the output file
output_file_path = 'Wav2Lip/Results/result_voice.mp4'

pad_top =  0
pad_bottom =  10
pad_left =  0
pad_right =  0
rescaleFactor =  1
nosmooth = True
use_hd_model = False
checkpoint_path = 'Wav2Lip/checkpoints/wav2lip.pth' if not use_hd_model else 'Wav2Lip/checkpoints/wav2lip_gan.pth'
inference_script_path = 'Wav2Lip/inference.py'

if nosmooth == False:
  !python $inference_script_path --checkpoint_path $checkpoint_path --face "$input_video_path" --audio "$input_audio_path" --pads $pad_top $pad_bottom $pad_left $pad_right --resize_factor $rescaleFactor
else:
  !python $inference_script_path --checkpoint_path $checkpoint_path --face "$input_video_path" --audio "$input_audio_path" --pads $pad_top $pad_bottom $pad_left $pad_right --resize_factor $rescaleFactor --nosmooth

# #Preview output video
if os.path.exists(output_file_path):
    !clear_output()
    print("Final Video Preview")
    print("Download this video from", output_file_path)

else:
    print("Processing failed. Output video not found.")