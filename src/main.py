from utils.contexts import Fun4Context
from utils.unicorn_gpt import UnicornGPT
from utils.speech2text import Speech2Text
from utils.text2speech import Text2Speech
from utils.run_env import RunEnv
from utils.usage_logger import log_time

if __name__ == "__main__":
    """
    Main entry point for the UnicornGPT application.
    Initializes the application, sets up the environment, and starts the main loop.
    Continuously listens for user input, processes it, 
    and generates responses until an error occurs or the user exits.
    """
    # Initialize the application
    # Change these parameters to your needs
    # =====================================
    execution_env = RunEnv.LOCAL  # or RunEnv.LOCAL, RunEnv.AZURE
    azure_model = "Ministral-3B"
    ollama_model = "llama3:latest"
    speach2text_model_path = "./data/models/vosk-model-en-us-0.42-gigaspeech"
    end_keyword = "please"
    # =====================================

    speech2text_engine = Speech2Text(speach2text_model_path, end_keyword)
    unicorn = UnicornGPT(
        execution=execution_env, azure_model=azure_model, ollama_model=ollama_model
    )

    while True:
        try:
            # Define character
            text2speech_engine = Text2Speech()  # within the loop to change voice
            sweets = Fun4Context.get_one()
            text2speech_engine.do("Choose your character.")
            character = speech2text_engine.init()
            introduction = f"I am a {character.description} and I love {sweets.value}. Ask me anything."
            text2speech_engine.do(introduction)

            # Get voice input
            message = speech2text_engine.do(character)
            print(f"Message: {message}")

            answer2everything = unicorn.chat(message, character, sweets)

            # Get voice output
            text2speech_engine.do(answer2everything)

            log_time()
            print("Done!")

        except Exception as err:
            print("Exiting... after error: ", err)
            break

        finally:
            log_time()
