import json
import os
from django.conf import settings

module_dir = os.path.dirname(__file__)
phonetic_json = os.path.join(module_dir, "phonetic.json")
with open(phonetic_json) as file:
    ipa_dict = json.load(file)


def eng_to_ipa(text):
    punctuations = {',': ' ,', '.': ' .', '!': ' !', ';': ' ;'}
    lower_text = text.translate(str.maketrans(punctuations)).lower()
    ans = " ".join(ipa_dict[i] if i in ipa_dict else i for i in lower_text.split())
    reverse_punctuation = {v: k for k, v in punctuations.items()}
    for k, v in reverse_punctuation.items():
        ans = ans.replace(k, v)  # De-modify punctuations
    return ans.capitalize()
