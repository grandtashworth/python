#!/home/grandt/PycharmProjects/Tarot/venv/bin/python

"""
__name__ = "Python 3 Card Tarot Spread"
__author__ = "Grandt Ashworth"
__date__ = "26 August 2020"
__version__ = "1.0"
"""

import random
import sys
import subprocess
import pkg_resources

required = {'pyfiglet', 'termcolor'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

from pyfiglet import Figlet
from termcolor import colored

number_of_cards_in_this_layout = int("3")

tarot_card_deck_dict = {
    "0": "The Fool",
    "1": "The Magician",
    "2": "The High Priestess",
    "3": "The Empress",
    "4": "The Emperor",
    "5": "The Hierophant",
    "6": "The Lovers",
    "7": "The Chariot",
    "8": "Justice",
    "9": "The Hermit",
    "10": "Wheel of Fortune",
    "11": "Strength",
    "12": "The Hanged Man",
    "13": "Death",
    "14": "Temperance",
    "15": "The Devil",
    "16": "The Tower",
    "17": "The Star",
    "18": "The Moon",
    "19": "The Sun",
    "20": "Judgement",
    "21": "The World",
    "22": "Ace of Wands",
    "23": "Two of Wands",
    "24": "Three of Wands",
    "25": "Four of Wands",
    "26": "Five of Wands",
    "27": "Six of Wands",
    "28": "Seven of Wands",
    "29": "Eight of Wands",
    "30": "Nine of Wands",
    "31": "Ten of Wands",
    "32": "Page of Wands",
    "33": "Knight of Wands",
    "34": "Queen of Wands",
    "35": "King of Wands",
    "36": "Ace of Pentacles",
    "37": "Two of Pentacles",
    "38": "Three of Pentacles",
    "39": "Four of Pentacles",
    "40": "Five of Pentacles",
    "41": "Six of Pentacles",
    "42": "Seven of Pentacles",
    "43": "Eight of Pentacles",
    "44": "Nine of Pentacles",
    "45": "Ten of Pentacles",
    "46": "Page of Pentacles",
    "47": "Knight of Pentacles",
    "48": "Queen of Pentacles",
    "49": "King of Pentacles",
    "50": "Ace of Cups",
    "51": "Two of Cups",
    "52": "Three of Cups",
    "53": "Four of Cups",
    "54": "Five of Cups",
    "55": "Six of Cups",
    "56": "Seven of Cups",
    "57": "Eight of Cups",
    "58": "Nine of Cups",
    "59": "Ten of Cups",
    "60": "Page of Cups",
    "61": "Knight of Cups",
    "62": "Queen of Cups",
    "63": "King of Cups",
    "64": "Ace of Swords",
    "65": "Two of Swords",
    "66": "Three of Swords",
    "67": "Four of Swords",
    "68": "Five of Swords",
    "69": "Six of Swords",
    "70": "Seven of Swords",
    "71": "Eight of Swords",
    "72": "Nine of Swords",
    "73": "Ten of Swords",
    "74": "Page of Swords",
    "75": "Knight of Swords",
    "76": "Queen of Swords",
    "77": "King of Swords",
}

tarot_card_meaning_dict = {
    "0": "New beginnings, optimism, trust in life",
    "1": "Action, the power to manifest",
    "2": "Inaction, going within, the mystical",
    "3": "Abundance, nurturing, fertility, life in bloom!",
    "4": "Structure, stability, rules and power",
    "5": "Institutions, tradition, society and its rules",
    "6": "Sexuality, passion, choice, uniting",
    "7": "Movement, progress, integration",
    "8": "Courage, subtle power, integration of animal self",
    "9": "Meditation, solitude, consciousness",
    "10": "Cycles, change, ups and downs",
    "11": "Fairness, equality, balance",
    "12": "Surrender, new perspective, enlightenment",
    "13": "The end of something, change, the impermeability of all things",
    "14": "Balance, moderation, being sensible",
    "15": "Destructive patterns, addiction, giving away your power",
    "16": "Collapse of stable structures, release, sudden insight",
    "17": "Hope, calm, a good omen!",
    "18": "Mystery, the subconscious, dreams",
    "19": "Success, happiness, all will be well",
    "20": "Rebirth, a new phase, inner calling",
    "21": "Completion, wholeness, attainment, celebration of life",
    "22": "New beginnings, creative spark, fertile ideas",
    "23": "Contemplation, assessing ones life direction",
    "24": "Reaping the rewards of your efforts",
    "25": "Celebration, safety, the home",
    "26": "Competition, minor struggles or disagreements",
    "27": "Success, accolades and achievement",
    "28": "Feeling defensive and on guard",
    "29": "Speed, things manifesting quickly",
    "30": "Pessimism, gearing up for the worst",
    "31": "Feeling oppressed, exhaustion, too many responsibilities",
    "32": "newly inspired, excited about life and work",
    "33": "An adventurous risk taker who follows his passions",
    "34": "Confidant, focused, has zest for life",
    "35": "Career focused, mature, passionate",
    "36": "Financial reward, clarity of life purpose, goals",
    "37": "Balance, multitasking",
    "38": "Meaningful work, enjoying one’s work, suitable career",
    "39": "Hoarding, feeling poor, holding self back out of fear",
    "40": "Minor money troubles, health problems, feeling like an outsider",
    "41": "Charity, accepting and giving help",
    "42": "Patience, waiting for your plans to bear fruit",
    "43": "Hard work, focused efforts, laying the groundwork",
    "44": "Luxury, rest, financial and material comforts",
    "45": "Financial success, strong business relationships",
    "46": "Student, commitment to learning",
    "47": "Cautious, sensible and slow to progress",
    "48": "Healthy in body and finances, grounded and calm",
    "49": "Enjoys the good life (food, drink and leisure), financially secure",
    "50": "Emotional fulfillment, joy",
    "51": "Partnership, mutual attraction, compatibility",
    "52": "Celebration, fun with friends, laughter",
    "53": "Boredom, dissatisfaction with what is being offered",
    "54": "Dwelling on the negative, self pity",
    "55": "Sentimentality, kindness, help",
    "56": "So many choices! Indecision, getting lost in fantasy",
    "57": "Abandoning something in search of something better",
    "58": "Indulgence, self-satisfaction",
    "59": "Emotional bliss, happiness, attainment",
    "60": "Creative, inspired, learning artistic skill",
    "61": "Romantic, adventurous, following one’s heart",
    "62": "Emotionally nurturing, intuitive, sensitive",
    "63": "Need to acknowledge deep feelings, avoid drowning out emotions",
    "64": "A fresh start, a sudden opportunity or idea, clarity",
    "65": "Indecision",
    "66": "Heartbreak, betrayal",
    "67": "Meditation, rest, retreat",
    "68": "Mind games, hostility",
    "69": "Leaving, accepting help, going somewhere better",
    "70": "Secret plans, abandoning ship",
    "71": "Feeling powerless and stuck",
    "72": "Overactive mind, anxiety",
    "73": "Feeling defeated, self sabotage",
    "74": "Mentally unstable or intellectually immature, acts without thinking",
    "75": "Fierce, determined, aggressively pursues goals",
    "76": "Intelligent, writer, communicative yet cold - cuts through B.S.",
    "77": "Serious, controlling, rational and mind/intellect-focused",
}

tarot_three_card_tense_dict = {
    "3": "......Past",
    "2": "...Present",
    "1": "....Future",
}
tarot_ten_card_tense_dict = {
    "1": "Significator",
    "2": "Challenge",
    "3": "Conscious",
    "4": "Subconscious",
    "5": "Past",
    "6": "Future",
    "7": "Attitude",
    "8": "Environment",
    "9": "Hopes and Fears",
    "10": "Final Outcome",
}

TarotReadingBanner = Figlet(font='ogre')
print(colored(TarotReadingBanner.renderText('Tarot Reading'), 'red', attrs=['bold']))

if number_of_cards_in_this_layout != len(tarot_three_card_tense_dict.keys()):
    pass
else:
    while number_of_cards_in_this_layout != 0:
        current_tarot_tense = tarot_three_card_tense_dict[str(number_of_cards_in_this_layout)]
        available_cards = tarot_card_deck_dict
        random_card = str(random.randrange(0, 77))
        if random_card in available_cards:
            selected_card = tarot_card_deck_dict[random_card]
            selected_meaning = tarot_card_meaning_dict[random_card]
            print(colored(current_tarot_tense.upper(), 'green', attrs=['bold']) + ' ' + '-' + ' ' + colored(selected_card, 'magenta', attrs=['bold']) + ' ' + '-' + ' ' + colored(selected_meaning, 'cyan'))
            del available_cards[random_card]
            number_of_cards_in_this_layout = int(number_of_cards_in_this_layout - 1)

print("")

