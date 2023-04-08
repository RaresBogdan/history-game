import openai
import requests


class OpenaiApi:
    def __init__(self):
        self.api_key = "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"
        pass

    def request_answer_openai(self, prompt, temperature, tokens):
        openai.api_key = self.api_key
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=temperature,
            max_tokens=tokens,
            best_of=1
        )

        return response.choices[0].text.strip()

    def get_a_list_of_answers(self, prompt, temperature, tokens):
        response_as_top = self.request_answer_openai(prompt, temperature, tokens)

        list_of_answers = response_as_top.split("\n")

        return list_of_answers

    def generate_dall_e_image(self, prompt):
        try:
            response = requests.post(
                "https://api.openai.com/v1/images/generations",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self.api_key}",
                },
                json={
                    "model": "image-alpha-001",
                    "prompt": prompt,
                    "num_images": 1,
                    "size": "1024x1024",
                    "response_format": "url",
                },
            )

            if response.status_code == 200:
                image_url = response.json()["data"][0]["url"]
                return image_url

            return None

        except Exception as e:
            print(f"Error generating DALL-E image: {e}")
            return None



