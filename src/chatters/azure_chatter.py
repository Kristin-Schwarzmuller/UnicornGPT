import os
from dotenv import load_dotenv

from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential

from chatters.chatter import Chatter


class AzureChatter(Chatter):

    def __init__(self):
        load_dotenv()
        AZURE_API_KEY = os.getenv("AZURE_API_KEY")
        ENDPOINT = os.getenv("AZURE_ENDPOINT")
        self.model_name = "Ministral-3B"

        self.model = ChatCompletionsClient(
            endpoint=ENDPOINT,
            credential=AzureKeyCredential(AZURE_API_KEY),
            api_version="2024-05-01-preview",
        )

    def chat(self, message: str, character: str, sweets: str) -> str:
        response = self.model.complete(
            messages=self.get_messages(character, sweets, message),
            max_tokens=2048,
            temperature=0.8,
            top_p=0.1,
            model=self.model_name,
        )

        return response.choices[0].message.content
