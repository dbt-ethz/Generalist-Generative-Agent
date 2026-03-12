import re


def to_snake_case(sentence):
    sentence = re.sub(r"[^\w\s]", "", sentence)
    sentence = sentence.replace(" ", "_")
    sentence = sentence.lower()
    return sentence
