import os
import tempfile

import sounddevice as sd
import soundfile as sf
import openai
from app.config import OPENAI_API_KEY

from app.logger import setup_logger

logger = setup_logger(__name__)

client = openai.OpenAI(api_key=OPENAI_API_KEY)

def text_to_speech(text):
    try:
        logger.info("Converting response to speech...")

        tts_response = client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=text,
            response_format="wav"
        )

        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio:
            temp_filename = temp_audio.name
            for chunk in tts_response.iter_bytes():
                temp_audio.write(chunk)

        data, samplerate = sf.read(temp_filename)
        sd.play(data, samplerate)
        sd.wait()
        logger.info("Playback complete.")

    except Exception as e:
        logger.error(f"Error during TTS playback: {e}")

    finally:
        if 'temp_filename' in locals() and os.path.exists(temp_filename):
            os.remove(temp_filename)
            logger.info("Temporary TTS audio file removed.")
