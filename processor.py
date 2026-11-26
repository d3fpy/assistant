from actions import actions
from models import Category, Command

questions = [
    "сколько",
    "скажи",
    "который",
    "какой сейчас",
    "какое сегодня",
    "подбрось",
    'кинь',
    'брось'
]


def execute(command):
    if command.category == Category.NONE:
        print("я глупенький")
        return

    for a in actions:
        if command.action in a[0]:
            print(a[1]())
            return
    print("я глупенький")


def process_and_execute(text):
    text = text.lower()
    command = Command(Category.NONE, "")
    for q in questions:
        if text.startswith(q):
            command.category = Category.QUESTION
            command.action = text[len(q):].strip(" ?.! ")
            break

    execute(command)
