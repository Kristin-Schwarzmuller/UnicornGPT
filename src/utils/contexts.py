import random
from enum import Enum


class Character4Context(Enum):
    """Character4Context" is an enumeration of whimsical characters that can be used
    in various applications, such as games or creative writing. Each character
    represents a playful and imaginative persona that can inspire creativity and joy."""

    UNICORN = ("Sparkly and Rainbow-Farting Unicorn", "unicorn")
    FLAMINGO = ("Flamingo", "flamingo")
    TWEEDY = ("Tweedy Bird", "tweedy")
    TURTLE = ("Wise and Slow-Moving Turtle", "turtle")
    LIZARD = ("Chill and Sunbathing Lizard", "lizard")
    BUNNY = ("Fluffy and Carrot-Craving Bunny", "bunny")
    LEMUR = ("Crazy looking Lemur", "lemur")
    PIRATE = ("Rowdy and Rum-Loving Pirate", "pirate")
    SCIENTIST = ("Mad and Sleep-Deprived Scientist", "scientist")
    ASTRONAUT = ("Spacey and Zero-Gravity-Loving Astronaut", "astronaut")
    ARTIST = ("Paint-Splattered and Overly-Abstract Artist", "artist")
    MUSICIAN = ("Offbeat and Melody-Mumbling Musician", "musician")
    ENGINEER = ("Over-Complicating and Gadget-Loving Engineer", "engineer")
    ROBOT = ("Beep-Booping and Overly-Literal Robot", "robot")
    ALIEN = ("Tentacled and UFO-Parking Alien", "alien")
    WIZARD = ("Bearded and Wand-Waving Wizard", "wizard")
    KNIGHT = ("Shiny-Armored and Dragon-Slaying Knight", "knight")
    VAMPIRE = ("Fang-Flashing and Garlic-Avoiding Vampire", "vampire")
    SUPERHERO = ("Cape-Wearing and Overly-Dramatic Superhero", "superhero")
    VILLAIN = ("Mustache-Twirling and Evil-Laughing Villain", "villain")
    FARMER = ("Overalls-Wearing and Tractor-Loving Farmer", "farmer")
    NINJA = ("Stealthy and Shadow-Lurking Ninja", "ninja")
    STEFAN = ("Stefan", "stefan")

    def __init__(self, description, keyword):
        self.description = description
        self.keyword = keyword

    @staticmethod
    def get_one():
        """Returns a random Character4Context."""
        return random.choice(list(Character4Context))


class Fun4Context(Enum):
    """Fun4Context" is an enumeration of fun and whimsical contexts that can be used
    in various applications, such as games or creative writing. Each context represents
    a playful and imaginative scenario that can inspire creativity and joy."""

    CHOCOLATE = "Chocolate"
    ICECREAM = "Ice Cream"
    CANDYFLOSS = "Candy Floss"
    RAINBOWS = "Rainbows"
    BUBBLES = "Bubbles"
    COOKIES = "Cookies"
    SPRINKLES = "Sprinkles"
    LEMONADE = "Lemonade"
    TRAMPOLINE = "Trampoline"
    POPCORN = "Popcorn"
    SPARKLERS = "Sparklers"
    FIREWORKS = "Fireworks"
    MILKSHAKE = "Milkshake"

    @staticmethod
    def get_one():
        """Returns a random Fun4Context."""
        return random.choice(list(Fun4Context))
