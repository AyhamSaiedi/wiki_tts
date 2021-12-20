from google.cloud import texttospeech_v1
from google.cloud import texttospeech
import os


def tts(input_text):

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'tts_google_cloud/gcloud_auth_key.json'

    # Instantiates a client
    client = texttospeech_v1.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech_v1.SynthesisInput(
        text=input_text)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech_v1.VoiceSelectionParams(
        language_code="de-DE", ssml_gender=texttospeech_v1.SsmlVoiceGender.NEUTRAL, name="de-DE-Wavenet-J"
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech_v1.AudioConfig(
        audio_encoding=texttospeech_v1.AudioEncoding.MP3
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # The response's audio_content is binary.
    with open("output.mp3", "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')


t = "Ach! So ein Scheiß. Oder auch nicht."
f = tts(t)
