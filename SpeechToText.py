from typing import Sequence
import google.cloud.texttospeech as tts
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "./spartan-trilogy-389714-f07d07c258e8.json"

class SpeechToText():
    def synthesize_text(self, text, output_file):
        #gets the client
        client = tts.TextToSpeechClient()
        # text input to be synthesized
        input_text = tts.SynthesisInput(text=text)
        # Sets the voice params
        voice = tts.VoiceSelectionParams(language_code="en-US", ssml_gender=tts.SsmlVoiceGender.FEMALE)
        # sets the audio config
        audio_config = tts.AudioConfig(audio_encoding=tts.AudioEncoding.MP3)

        # requests the audio
        response = client.synthesize_speech(request={"input": input_text, "voice": voice, "audio_config": audio_config})

        #writes the audio content
        with open(output_file, "wb") as out:
            out.write(response.audio_content)
            print(f'Audio content written to "{output_file}"')