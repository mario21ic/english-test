#!/usr/bin/env python

import random

def main():
    tenses = ["simple present", "simple past", "simple future", \
            "present continuous", "past continuous", "future continuous", \
            "present perfect", "past perfect", "future perfect", \
            "present perfect continuous", " perfect continuous", "future perfect continuous"]
    modals =["would", "reported"]
    forms = ["affirmative", "negative", "subject question", "object question"]
    subject_pronouns = ["I", "you", "he", "she", "it", "we", "they"]

    print("Make a sentense in %s form with %s and %s tense" % (random.choice(forms), random.choice(subject_pronouns), random.choice(tenses)))


if __name__ == "__main__":
    main()
