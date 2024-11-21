import commentjson
from openai import OpenAI

API_KEY = "YOUR_API_KEY"

def doTranslateGPT(_targetJSON):
    gptObj = OpenAI(
        api_key=API_KEY
    )
    
    response = gptObj.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role":"system","content":"당신은 게임전문 번역가입니다. 번역하고자 하는 게임은 마인크래프트입니다."},
            {"role":"system","content":"딕셔너리 형태의 데이터를 넘겨드릴겁니다. Key값은 그대로두고 Value값만 번역해야합니다."},
            {"role":"system","content":"영어를 한글로 번역하는 작업이며, 답변은 Json 형태로만 주시면 됩니다."},
            {"role":"user","content":_targetJSON}
        ]
    )
    
    translated_json_str = response.choices[0].message.content
   
    result = translated_json_str[7:-3].strip()

    translated_data = commentjson.loads(result)
    
    return translated_data

def doTranslateGoogle():
    pass
