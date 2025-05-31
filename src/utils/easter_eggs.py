from dataclasses import dataclass


@dataclass
class EasterEgg:
    """
    Class to represent an Easter egg with keywords and a response.
    """

    keywords: list[str]
    what_to_say: str


class EasterEggs:
    """
    Class to handle Easter eggs in the application.
    """

    def __init__(self):
        self.easter_eggs = [
            EasterEgg(["cat"], "No complicated conversations please!"),
            EasterEgg(["tool"], "The VST has yet to be invented that can do this"),
            EasterEgg(
                ["moon", "line"], "Wait, I Maybe I have a app for that. Let me check."
            ),
            EasterEgg(["better"], "Maybe I have a plugin for that"),
            EasterEgg(
                ["sound", "engineer"],
                "You have to understand how to set the compressor correctly",
            ),
            EasterEgg(["new", "track"], "30 minutes without saving is a hefty move"),
            EasterEgg(["bunny"], "Gunni bunny, Gunni bunny, Gunni bunny, Gunni bunny"),
            EasterEgg(["high", "acid"], "Ok now, who is gonna get him down?"),
            EasterEgg(
                ["backpack"],
                "My backpack is too big? Oh I am sorry, Sir! It must be all the sweets",
            ),
            EasterEgg(["boring"], "Borrrring? Ring Ring ring ring. Borrrring!"),
            EasterEgg(["good", "day"], "Tachchen you dumb mother fucker"),
            EasterEgg(["moon"], "What? Did i hear Moon? Always brings me so high!"),
            EasterEgg(
                ["ayahuasca"],
                "You wanna find yourself? Alright, but did you prepare your Excel sheet?",
            ),
            EasterEgg(["double"], "Double wougle, hihihihihihihihi"),
            EasterEgg(["engine"], "Engine"),
            EasterEgg(
                ["Maffay"],
                "I would love to answer that but You stole all the words. Shutting down now.",
            ),
            EasterEgg(
                ["Feta"],
                "Catherine Feta Jones my name, nice to meet you? Do you have cheese?",
            ),
            EasterEgg(
                ["lion", "king"],
                "Mufasa! The circle of life... Or the circle of candies?",
            ),
            EasterEgg(["extra"], "Raggadagga, Raggadagga, Raggadagga"),
            EasterEgg(
                ["shovel"],
                "Sorry I did not get that. Do you mean, your majesty King shovel the first? ",
            ),
            EasterEgg(["math"], "Triangular."),
            EasterEgg(["favorite", "animal"], "No, i never loved the Peacock?"),
            EasterEgg(["food"], "One more bite! One more bite!"),
        ]
