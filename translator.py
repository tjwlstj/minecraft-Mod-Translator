import commentjson
import openai
import logging

API_KEY = "YOUR_API_KEY"

def do_translate_gpt(target_json, logger=None):
    """
    Translates JSON data using OpenAI GPT.

    Args:
        target_json (str): JSON data as a string to be translated.
        logger (logging.Logger): Optional logger for logging translation status.

    Returns:
        dict: Translated JSON data.
    """
    if logger:
        logger.info("Starting translation using GPT.")

    # Initialize OpenAI API
    openai.api_key = API_KEY

    try:
        response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role":"system","content":"당신은 게임전문 번역가입니다. 번역하고자 하는 게임은 마인크래프트입니다."},
            {"role":"system","content":"딕셔너리 형태의 데이터를 넘겨드릴겁니다. Key값은 그대로두고 Value값만 번역해야합니다."},
            {"role":"system","content":"영어를 한글로 번역하는 작업이며, 답변은 Json 형태로만 주시면 됩니다."},
            {"role":"user","content":target_json}
        ]
    )
        if logger:
            logger.info("Translation request successfully sent to OpenAI.")

        # Extract translated JSON string
        translated_json_str = response.choices[0].message.content

        if logger:
            logger.debug(f"Raw translated response: {translated_json_str}")

        # Safely parse JSON result
        translated_data = commentjson.loads(translated_json_str[7:-3].strip())
        if logger:
            logger.info("Translation successfully parsed into JSON format.")

        return translated_data

    except Exception as e:
        if logger:
            logger.error(f"An error occurred during translation: {e}")
        raise