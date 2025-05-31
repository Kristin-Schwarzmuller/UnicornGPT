from utils.run_env import RunEnv
from utils.contexts import Character4Context, Fun4Context
from utils.easter_eggs import EasterEggs
from chatters.azure_chatter import AzureChatter
from chatters.ollama_chatter import OllamaChatter

class UnicornGPT:
    
    def __init__(self, execution: RunEnv, azure_model: str, ollama_model: str) -> None:
        """
        Initialize the UnicornGPT with specified execution environment and models.

        Parameters
        ----------
        execution : RunEnv
            The execution environment (e.g., LOCAL, AZURE).
        azure_model : str
            The model name for Azure execution.
        ollama_model : str
            The model name for Ollama execution.

        Returns
        -------
        None
        """
        self.azure_model = azure_model
        self.execution = execution
        self.easter_eggs = EasterEggs()
        if self.execution == RunEnv.LOCAL:
            self.chatter = OllamaChatter()
        elif self.execution == RunEnv.AZURE:
            self.chatter = AzureChatter()

    def chat(
        self, message: str, character: Character4Context, sweets: Fun4Context
    ) -> str:
        """
        Generate a chat response based on the message, character, and sweets context.
        Parameters
        ----------
        message : str
            The input message to process.
        character : Character4Context
            The character context for the chat.
        sweets : Fun4Context
            The sweets context for the chat.
        Returns
        -------
        str
            The generated chat response.
        """
        if not isinstance(character, Character4Context):
            raise ValueError("Character must be an instance of Character4Context")
        if not isinstance(sweets, Fun4Context):
            raise ValueError("Sweets must be an instance of Fun4Context")

        character = character.value
        sweets = sweets.value

        if not message:
            message = f"Write a poem about {sweets} you as a {character}."

        for egg in self.easter_eggs.easter_eggs:
            if all(keyword in message.lower() for keyword in egg.keywords):
                return egg.what_to_say
        
        return self.chatter.chat(message, character, sweets)




