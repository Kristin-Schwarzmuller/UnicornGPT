import vosk
import pyaudio
import json

from utils.contexts import Character4Context


class Speech2Text:

    def __init__(self, model_path: str, end_keyword: str) -> None:
        """
        Initialize the Speech2Text class with a Vosk model and end keyword.
        Parameters
        ----------
        model_path : str
            Path to the Vosk model directory.
        end_keyword : str
            Keyword to stop the speech recognition.
        Returns
        -------
        None
        """
        self.END_KEYWORD = end_keyword
        self.__model = vosk.Model(model_path)
        self.__rec = vosk.KaldiRecognizer(self.__model, 16000)
        self.__p = pyaudio.PyAudio()

        # Open the microphone stream with specific device index (microphone 1)
        self.__stream = self.__p.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=16000,
            input=True,
            input_device_index=1,  # Select microphone 1
            frames_per_buffer=4096,
        )
        

    def __listen(self) -> str:
        data = self.__stream.read(
            4096, exception_on_overflow=False
        )  # read in chunks of 4096 bytes
        if self.__rec.AcceptWaveform(data):  # accept waveform of input voice
            result = json.loads(self.__rec.Result())
            recognized_text = result["text"]
            print(f"Recognized text: {recognized_text}")
            return recognized_text

        return ""
    
    def __detect_character(self, recognized_text: str) -> Character4Context | None:
        if not recognized_text:
            return None
        for character in Character4Context:
            if character.keyword in recognized_text.lower():
                print(f"Recognized character: {character.description}")
                return character
        return None

    def init(self) -> Character4Context: 
        """
        Initialize the speech recognition by listening for a character keyword.
        Returns
        -------
        Character4Context
            The recognized character context.
        """
        recognized_text = ""
        character = None
        while not character:
            recognized_text = self.__listen()
            character = self.__detect_character(recognized_text)
        
        return character

    def do(self, character: Character4Context) -> str:
        """
        Record a message from the character keyword until the end keyword is spoken.
        Parameters
        ----------
        character : Character4Context
            The character context to recognize.
        Returns
        -------
        str
            The recorded message.
        """
        message = ""
        while not character.keyword in message.lower():
            message = self.__listen()

        print(f"Recording... Say {self.END_KEYWORD} to stop.")
        while not self.END_KEYWORD in message.lower():
            recognized_text = self.__listen()
            message += " " + recognized_text

        return message
