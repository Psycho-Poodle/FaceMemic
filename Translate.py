# !pip install googletrans==4.0.0-rc1
from Whisper import extracted_text
from googletrans import Translator

def translate_text(text, target_language='en'):
    translator = Translator()

    # Translate the text
    translation = translator.translate(text, dest=target_language)

    # Return the translated text
    return translation.text

# Example usage:
text_to_translate = extracted_text
translated_text = translate_text(text_to_translate, target_language='en')
print(translated_text)