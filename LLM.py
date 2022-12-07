#based from https://www.twilio.com/blog/openai-gpt-3-chatbot-python-twilio-sms

#note: gpt-3 ; model: text-davinci-003  ito 
#ang latest na nirecommend ni sir ay ChatGPT > GPT3 [ https://chat.openai.com/chat ]

#OPENAI_KEY=#your-openai-api-key-here

OPENAI_KEYS = []

import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.environ.get('OPENAI_KEY')
completion = openai.Completion()

start_chat_log = 'HEY SIRI' #ano yung gusto nating pang-signal sa assistant natin?

def ask(question, chat_log=None):

#    if chat_log is None:
#       chat_log = start_chat_log
#di ko sure kung need yung two lines na nasa taas nito
    prompt = f'{chat_log}Human: {question}\nAI:' #kunin mula sa asr yung text para maging prompt
    #prompt = f'{chat_log}Human: {question}\nAI:' #kunin mula sa asr yung text para maging prompt
    response = completion.create(
        prompt=prompt, engine="davinci", stop=['\nHuman'], temperature=0.9,
        top_p=1, frequency_penalty=0, presence_penalty=0.6, best_of=1, max_tokens=150)
    answer = response.choices[0].text.strip()
    return answer

#paano gamitin? 
#ilagay sa terminal: ask('Who played Forrest Gump in the movie?')
#output: 'Oh my, that is a tough one! Forrest Gump was played by Tom Hanks.'
#bale, gagamitin ang text to speech para basahin yung sagot niya