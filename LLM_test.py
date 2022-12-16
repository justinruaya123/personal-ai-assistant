import openai

openai.api_key = "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"
class LLM_test:
    def generate_response(prompt):
        model_engine = "text-davinci-002"
        prompt = (f"{prompt}")

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
