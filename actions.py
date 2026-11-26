import datetime
import random


def coin():
    return random.choice(['орёл', 'решка'])


def time():
    return datetime.datetime.now().strftime("%H:%M")


actions = [
    (['монету', 'монетку'], coin),
    (["время", "час", "времени"], time),
    (["число", "дата", "день", "дату"], datetime.date.today),
]
