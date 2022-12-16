#based from https://www.twilio.com/blog/openai-gpt-3-chatbot-python-twilio-sms

#note: gpt-3 ; model: text-davinci-003  ito 
#ang latest na nirecommend ni sir ay ChatGPT > GPT3 [ https://chat.openai.com/chat ]

#OPENAI_KEY=#your-openai-api-key-here

#OPENAI_KEYS = []
#import openai

#openai.api_key = "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"

#completion = openai.Completion()

#def GPT3(question, chat_log=None):

  #  prompt = question

   # response = completion.create(
   #     prompt=prompt, engine="davinci", stop=['\nHuman'], temperature=0.9,
    #top_p=1, frequency_penalty=0, presence_penalty=0.6, best_of=1, max_tokens=150)
  #  answer = response.choices[0].text.strip()

    #return answer

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from chatgpt import Conversation



conversation = Conversation()

conversation.chat(input_text)
