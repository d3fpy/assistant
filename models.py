from dataclasses import dataclass
from enum import Enum


class Category(Enum):
    NONE = 0
    QUESTION = 1
    EXECUTE = 2


@dataclass
class Command:
    category: Category # категория действия
    action:   str      # предмет действия
