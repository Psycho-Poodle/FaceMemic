import subprocess

# def run_clone():
    # subprocess.run(['python', 'Models/Clone.py'])

def run_whisper():
    subprocess.run(['python', 'Whisper.py'])

def run_translate():
    subprocess.run(['python', 'Translate.py'])

def run_11lab():
    subprocess.run(['python', '11Lab.py'])

def run_wav2lip():
    subprocess.run(['python', 'Wav2Lip.py'])

def main():
    # run_clone()
    run_whisper()
    run_translate()
    run_11lab()
    run_wav2lip()

if __name__ == "__main__":
    main()
