import os
import tempfile

import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
import openai


from app.config import OPENAI_API_KEY, FS, CHUNK_DURATION, SILENCE_DURATION, SILENCE_THRESHOLD

from app.logger import setup_logger
logger = setup_logger(__name__)


client = openai.OpenAI(api_key=OPENAI_API_KEY)

def speech_to_text():
    logger.info("Speak now... Recording will stop after 3 seconds of silence.")
    recorded_audio = []
    silent_chunks = 0

    try:
        while True:
            chunk = sd.rec(
                int(CHUNK_DURATION * FS),
                samplerate=FS,
                channels=1,
                dtype='int16'
            )
            sd.wait()
            volume = np.abs(chunk).mean()
            recorded_audio.append(chunk)

            if volume < SILENCE_THRESHOLD:
                silent_chunks += 1
            else:
                silent_chunks = 0

            if silent_chunks * CHUNK_DURATION >= SILENCE_DURATION:
                logger.info("Silence detected. Stopping recording.")
                break

    except KeyboardInterrupt:
        logger.warning("Recording interrupted by user.")

    audio_data = np.concatenate(recorded_audio, axis=0)

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio:
        temp_filename = temp_audio.name
        write(temp_filename, FS, audio_data)

    try:
        logger.info("Transcribing your audio...")
        with open(temp_filename, "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )

        logger.info(f"Transcription: {transcription.text}")
        return transcription.text

    finally:
        if os.path.exists(temp_filename):
            os.remove(temp_filename)
            logger.info("Temporary audio file removed.")
