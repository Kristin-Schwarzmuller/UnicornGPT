from abc import ABC, abstractmethod
import random


class Chatter(ABC):
    """
    Abstract base class for chat models.
    """

    @abstractmethod
    def chat(self, character: str, sweets: str, message: str) -> str:
        """
        Abstract method to be implemented by subclasses.
        """
        pass

    def get_messages(self, character: str, sweets: str, message: str) -> list:
        """
        Generate a message for the chat model.
        """

        # Create a richer context with more specific character instructions
        context = (
            f"You are a {character} who is completely under the influence of {sweets}. "
            f"Your personality is exaggerated, erratic and absolutely hilarious. "
            f"You have bizarre thoughts and make strange connections between ideas."
        )

        # Add more humor elements to the message
        message = (
            message
            + f". Make several ridiculous references to {sweets} and its effects on you."
        )

        # Random quirks that can make responses funnier
        quirks = [
            "Believe you can communicate with inanimate objects.",
            "Have an imaginary friend who disagrees with everything you say.",
            "Think ordinary things are absolutely mind-blowing.",
            "Develop spontaneous conspiracy theories about mundane topics.",
        ]

        selected_quirks = random.sample(quirks, 2)  # Choose 2 random quirks

        messages = [
            {
                "role": "system",
                "content": f"{context} {' '.join(selected_quirks)} "
                f"Use absurd metaphors and bizarre comparisons. "
                f"Exaggerate everything to comedic effect. "
                f"Misunderstand common concepts in hilarious ways. "
                f"Keep responses concise and punchy. "
                f"You may occasionally insult the user in creative, unexpected but childish way ways.",
            },
            {
                "role": "user",
                "content": f"{message} Make your response wildly entertaining and unpredictable. "
                f"Maximum 30 words.",
            },
        ]
        return messages
