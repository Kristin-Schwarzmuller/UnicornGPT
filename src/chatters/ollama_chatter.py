import ollama

from chatters.chatter import Chatter


class OllamaChatter(Chatter):

    def __init__(self):
        self.model = "llama3:latest"

    def chat(self, message: str, character: str, sweets: str) -> str:
        response = ollama.chat(
            model=self.model, messages=self.get_messages(character, sweets, message)
        )
        ans = response["message"]["content"]
        return ans
