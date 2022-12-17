import openai

openai.api_key = "sk"+ "-" + "759DgHTJW" + "UQSDxw4GpYQT" + "3BlbkFJ3tCCf0" + "kKM4ki33LONyrw"
def setKey(key):
    openai.api_key = key

def generate_response(text):
    model_engine = "text-davinci-002"
    prompt = (f"{text}")

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
     n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text

    return message.strip()
