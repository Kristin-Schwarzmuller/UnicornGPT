# https://github.com/n1teshy/yapper-tts
import random
from yapper import PiperSpeaker, PiperVoiceGB


class Text2Speech:

    def __init__(self) -> None:
        """
        Initialize the Text2Speech3 class.
        """
        self.voice = random.choice(list(PiperVoiceGB))
        self.speaker = PiperSpeaker(voice=self.voice)

    def do(self, answer: str) -> None:
        """
        Convert text to speech and play it.
        Parameters
        ----------
        answer : str
            The text to be converted to speech.
        Returns
        -------
        None
        """
        print(answer)
        self.speaker.say(answer)
