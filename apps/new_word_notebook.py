import json
import logging
import os
import random

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

new_words = []


def load_new_words(filepath: str):
    global new_words
    if os.path.exists(filepath):
        with open(filepath) as input_file:
            new_words = json.load(input_file)
    else:
        logger.error(f'the new word file {filepath} was not exist')
        new_words = []


def get_random_new_word() -> str:
    index = random.randint(0, len(new_words) - 1)
    return new_words[index]
