import numpy as np
import openai

from app.stt import speech_to_text
from app.tts import text_to_speech
from app.config import prompt, OPENAI_API_KEY
from app.logger import setup_logger

logger = setup_logger(__name__)

client = openai.OpenAI(api_key=OPENAI_API_KEY)


def main():
    logger.info("Voice assistant started. Press Ctrl+C to stop.")

    try:
        while True:
            user_text = speech_to_text()

            if not user_text.strip():
                logger.info("No input detected. Try again.")
                continue

            logger.info("Getting AI response...")
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": user_text}
                ]
            )

            ai_reply = response.choices[0].message.content
            logger.info(f"AI Response: {ai_reply}")

            text_to_speech(ai_reply)

    except KeyboardInterrupt:
        logger.info("Assistant stopped by user.")


if __name__ == "__main__":
    main()
